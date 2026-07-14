from src.application.neural_service import NeuralApplicationService
from src.infrastructure.logger import CanonicalLogger

class NeuralCLI:
    """
    Canon X - Interface Layer: Presentation and user interaction.
    """
    def __init__(self, input_shape=10):
        self.service = NeuralApplicationService(input_shape)
        self.logger = CanonicalLogger()

    def run(self):
        while True:
            print("\n=== Neural Protection System (Canonical) ===")
            print("1. Run Inference")
            print("2. Train Model")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                data, result = self.service.execute_inference()
                self.logger.info(f"Inference result: {result}")
            elif choice == '2':
                self.service.execute_training()
                self.logger.info("Model trained successfully.")
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    cli = NeuralCLI()
    cli.run()
