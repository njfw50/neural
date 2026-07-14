from src.domain.neural_model import NeuralModelDomain
import numpy as np

class NeuralApplicationService:
    """
    Canon X - Application Layer: Use cases and system coordination.
    """
    def __init__(self, input_shape):
        self.domain = NeuralModelDomain(input_shape)

    def execute_inference(self):
        # Business logic for inference use case
        new_data = np.random.random((1, self.domain.input_shape))
        result = self.domain.predict(new_data)
        return new_data, result

    def execute_training(self):
        # Business logic for training use case
        data = np.random.random((100, self.domain.input_shape))
        labels = np.random.randint(2, size=100)
        self.domain.train(data, labels)
        return True
