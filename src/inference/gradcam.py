from pathlib import Path

import cv2
import numpy as np
import tensorflow as tf

from src.inference.image_utils import (
    preprocess_image,
    pil_to_numpy,
)


class GradCAM:

    def __init__(
        self,
        model,
        backbone_name="efficientnetb0",
        last_conv_layer_name="top_conv",
    ):
        self.model = model

        self.backbone = model.get_layer(backbone_name)

        self.last_conv_layer = self.backbone.get_layer(
            last_conv_layer_name
        )

    def generate_heatmap(self, image, class_index=None):
        """
        Generate Grad-CAM heatmap.

        Parameters
        ----------
        image : tf.Tensor
            Shape (1,224,224,3)

        class_index : int | None

        Returns
        -------
        heatmap
        predictions
        predicted_class
        """

        feature_extractor = tf.keras.Model(
            inputs=self.backbone.input,
            outputs=self.last_conv_layer.output,
        )

        with tf.GradientTape() as tape:

            feature_maps = feature_extractor(
                image,
                training=False,
            )

            tape.watch(feature_maps)

            x = feature_maps

            x = self.backbone.get_layer("top_bn")(x)

            x = self.backbone.get_layer("top_activation")(x)

            x = self.model.get_layer(
                "global_average_pooling2d_1"
            )(x)

            x = self.model.get_layer(
                "dense_2"
            )(x)

            x = self.model.get_layer(
                "dropout_1"
            )(x, training=False)

            predictions = self.model.get_layer(
                "dense_3"
            )(x)

            if class_index is None:
                class_index = tf.argmax(predictions[0])

            class_score = predictions[:, class_index]

        gradients = tape.gradient(
            class_score,
            feature_maps,
        )

        pooled_gradients = tf.reduce_mean(
            gradients,
            axis=(0, 1, 2),
        )

        feature_maps = feature_maps[0]

        heatmap = tf.reduce_sum(
            feature_maps * pooled_gradients,
            axis=-1,
        )

        heatmap = tf.maximum(heatmap, 0)

        heatmap = heatmap / (
            tf.reduce_max(heatmap) + 1e-8
        )

        return (
            heatmap.numpy(),
            predictions.numpy(),
            int(class_index),
        )

    def overlay_heatmap(
        self,
        original_image,
        heatmap,
        alpha=0.4,
    ):
        """
        Overlay Grad-CAM heatmap on image.
        """

        if hasattr(original_image, "convert"):
            image = pil_to_numpy(original_image)
        else:
            image = original_image.copy()

        h, w = image.shape[:2]

        heatmap = cv2.resize(
            heatmap,
            (w, h),
        )

        heatmap = np.uint8(255 * heatmap)

        colored = cv2.applyColorMap(
            heatmap,
            cv2.COLORMAP_JET,
        )

        colored = cv2.cvtColor(
            colored,
            cv2.COLOR_BGR2RGB,
        )

        overlay = cv2.addWeighted(
            image,
            1 - alpha,
            colored,
            alpha,
            0,
        )

        return overlay

    def explain(
        self,
        image,
        class_index=None,
        alpha=0.4,
    ):
        """
        Complete Grad-CAM pipeline.

        Parameters
        ----------
        image : PIL.Image

        Returns
        -------
        overlay
        predictions
        predicted_class
        heatmap
        """

        image_tensor = preprocess_image(image)

        heatmap, predictions, predicted_class = (
            self.generate_heatmap(
                image_tensor,
                class_index,
            )
        )

        overlay = self.overlay_heatmap(
            image,
            heatmap,
            alpha,
        )

        return (
            overlay,
            predictions,
            predicted_class,
            heatmap,
        )