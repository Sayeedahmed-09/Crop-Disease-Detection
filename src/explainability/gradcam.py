import tensorflow as tf
import numpy as np
import matplotlib.cm as cm


def get_last_conv_layer(model):
    base_model = model.get_layer("efficientnetb0")

    for layer in reversed(base_model.layers):
        if isinstance(layer, tf.keras.layers.Conv2D):
            return layer.name

    raise ValueError("No Conv2D layer found.")


def make_gradcam_heatmap(img_array, model):
    last_conv_layer_name = get_last_conv_layer(model)

    base_model = model.get_layer("efficientnetb0")

    grad_model = tf.keras.models.Model(
        inputs=model.inputs,
        outputs=[
            base_model.get_layer(last_conv_layer_name).output,
            model.output,
        ],
    )

    with tf.GradientTape() as tape:

        conv_outputs, predictions = grad_model(img_array)

        pred_index = tf.argmax(predictions[0])

        class_channel = predictions[:, pred_index]

    grads = tape.gradient(class_channel, conv_outputs)

    pooled_grads = tf.reduce_mean(
        grads,
        axis=(0, 1, 2),
    )

    conv_outputs = conv_outputs[0]

    heatmap = conv_outputs @ pooled_grads[..., tf.newaxis]

    heatmap = tf.squeeze(heatmap)

    heatmap = tf.maximum(
        heatmap,
        0,
    ) / tf.math.reduce_max(heatmap)

    return heatmap.numpy()


def overlay_heatmap(image, heatmap, alpha=0.4):

    heatmap = np.uint8(255 * heatmap)

    jet = cm.get_cmap("jet")

    jet_colors = jet(np.arange(256))[:, :3]

    jet_heatmap = jet_colors[heatmap]

    jet_heatmap = tf.keras.utils.array_to_img(jet_heatmap)

    jet_heatmap = jet_heatmap.resize(
        (image.size[0], image.size[1])
    )

    jet_heatmap = tf.keras.utils.img_to_array(jet_heatmap)

    image = tf.keras.utils.img_to_array(image)

    superimposed = jet_heatmap * alpha + image

    superimposed = tf.keras.utils.array_to_img(superimposed)

    return superimposed