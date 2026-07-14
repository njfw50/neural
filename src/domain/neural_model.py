import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

class NeuralModelDomain:
    """
    Canon X - Domain Layer: Pure core logic for the neural model.
    """
    def __init__(self, input_shape):
        self.input_shape = input_shape
        self.model = self._build_model()

    def _build_model(self):
        model = Sequential([
            Dense(64, activation='relu', input_shape=(self.input_shape,)),
            Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        return model

    def predict(self, data):
        return self.model.predict(data)

    def train(self, data, labels, epochs=10):
        return self.model.fit(data, labels, epochs=epochs)
