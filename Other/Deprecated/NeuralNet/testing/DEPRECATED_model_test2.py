import tensorflow as tf
from tensorflow.keras import layers, models
import tensorflow_hub as hub
from tensorflow.keras.metrics import BinaryAccuracy, Precision, Recall, F1Score
import tensorflow_addons as tfa


class TextClassificationModel:
    def __init__(
        self,
        num_classes,
        use_pretrained_embeddigns=True,
        max_features=None,
        embedding_dim=16,
        sequence_length=500,
    ):
        self.num_classes = num_classes
        self.use_pretrained_embeddings = use_pretrained_embeddigns
        self.max_features = max_features
        self.embedding_dim = embedding_dim
        self.sequence_length = sequence_length
        self.model = self.build_model()

    def build_model(self):
        model = models.Sequential()
        if self.use_pretrained_embeddings:
            embedding_layer = hub.KerasLayer(
                "https://tfhub.dev/google/universal-sentence-encoder/4",
                input_shape=[],
                dtype=tf.string,
                trainable=False,
            )
            model.add(embedding_layer)
        else:
            model.add(
                layers.Embedding(
                    input_dim=self.max_features,
                    output_dim=self.embedding_dim,
                    input_length=self.sequence_length,
                )
            )
            model.add(layers.Dropout(0.2))
            model.add(layers.GlobalAveragePooling1D())

        model.add(layers.Dense(128, activation="relu"))
        model.add(layers.Dropout(0.2))
        model.add(layers.Dense(self.num_classes, activation="sigmoid"))

        return model

    def compile_model(self):
        self.model.compile(
            optimizer="adam",
            loss="binary_crossentropy",
            metrics=[
                BinaryAccuracy(name="accuracy"),
                tf.keras.metrics.Precision(name="precision"),
                tf.keras.metrics.Recall(name="recall"),
            ],
        )

    def train_model(self, train_dataset, val_dataset, epochs=10):
        self.model.fit(train_dataset, epochs=epochs, validation_data=val_dataset)

    def get_model(self):
        return self.model
