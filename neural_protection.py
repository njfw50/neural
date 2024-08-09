import numpy as np  # Importa o NumPy para operações numéricas
from tensorflow.keras.models import Sequential  # Importa a classe Sequential do Keras
from tensorflow.keras.layers import Dense  # Importa a camada Dense do Keras

# Classe principal do sistema de proteção neural
class NeuralProtectionSystem:
    def __init__(self, input_shape):
        self.input_shape = input_shape  # Define o formato de entrada para o modelo
        self.model = self.build_model()  # Chama o método para construir o modelo

    # Método para construir o modelo neural
    def build_model(self):
        model = Sequential([  # Cria um modelo sequencial
            Dense(64, activation='relu', input_shape=(self.input_shape,)),  # Primeira camada densa com 64 neurônios
            Dense(1, activation='sigmoid')  # Camada de saída com 1 neurônio, ativação sigmoide
        ])
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])  # Compila o modelo
        return model  # Retorna o modelo construído

    # Método para exibir o menu principal do sistema
    def show_menu(self):
        print("=== Neural Protection System Menu ===")  # Exibe o título do menu
        print("1. Run Inference")  # Opção para rodar a inferência no modelo
        print("2. Train Model")  # Opção para treinar o modelo
        print("3. Exit")  # Opção para sair do sistema
        choice = input("Choose an option: ")  # Recebe a escolha do usuário
        self.handle_choice(choice)  # Chama o método que lida com a escolha

    # Método que lida com a escolha do menu
    def handle_choice(self, choice):
        if choice == '1':
            self.run_inference()  # Chama o método de inferência
        elif choice == '2':
            self.train_model()  # Chama o método de treinamento
        elif choice == '3':
            print("Exiting...")  # Exibe mensagem e finaliza o programa
        else:
            print("Invalid choice, please try again.")  # Exibe erro e retorna ao menu
            self.show_menu()  # Reexibe o menu para nova escolha

    # Método para executar uma inferência no modelo
    def run_inference(self):
        print("Running inference...")  # Informa que a inferência está em andamento
        new_data = np.random.random((1, self.input_shape))  # Simula a criação de dados de entrada
        result = self.model.predict(new_data)  # Realiza a inferência no modelo
        print(f"Inference result: {result}")  # Exibe o resultado da inferência
        self.show_menu()  # Retorna ao menu principal

    # Método para treinar o modelo
    def train_model(self):
        print("Training model...")  # Informa que o treinamento está em andamento
        data = np.random.random((100, self.input_shape))  # Simula a criação de dados de treinamento
        labels = np.random.randint(2, size=100)  # Simula a criação de rótulos de treinamento
        self.model.fit(data, labels, epochs=10)  # Treina o modelo com os dados simulados
        print("Model trained successfully.")  # Informa que o treinamento foi concluído
        self.show_menu()  # Retorna ao menu principal

# Exemplo de uso do sistema
if __name__ == "__main__":
    input_shape = 10  # Define o formato de entrada para o modelo
    protection_system = NeuralProtectionSystem(input_shape)  # Inicializa o sistema de proteção
    protection_system.show_menu()  # Exibe o menu do sistema
