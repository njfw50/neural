from neural_debugger import NeuralDebugger  # Importa o módulo de depuração avançada
from neural_self_adjust import NeuralSelfAdjust  # Importa o módulo de autoajuste
import numpy as np  # Importa o NumPy para operações numéricas

# Classe principal do sistema de proteção neural, integrando depuração e autoajuste
class NeuralProtectionSystem:
    def __init__(self, model, input_shape):
        self.model = model  # Armazena o modelo neural que será protegido e ajustado
        self.input_shape = input_shape  # Define o formato de entrada para o modelo
        self.debugger = NeuralDebugger()  # Inicializa o debugger para monitoramento detalhado
        self.self_adjuster = NeuralSelfAdjust(self.model)  # Inicializa o autoajustador para autocorreção e aprimoramento

    # Método para exibir o menu principal do sistema
    def show_menu(self):
        print("=== Neural Protection System Menu ===")  # Exibe o título do menu
        print("1. Run Inference")  # Opção para rodar a inferência no modelo
        print("2. Train Model")  # Opção para treinar o modelo
        print("3. Debug Model")  # Opção para iniciar a depuração do modelo
        print("4. Auto-Adjust Model")  # Opção para autoajustar o modelo
        print("5. Exit")  # Opção para sair do sistema
        choice = input("Choose an option: ")  # Recebe a escolha do usuário
        self.handle_choice(choice)  # Chama o método que lida com a escolha

    # Método que lida com a escolha do menu
    def handle_choice(self, choice):
        if choice == '1':
            self.run_inference()  # Chama o método de inferência
        elif choice == '2':
            self.train_model()  # Chama o método de treinamento
        elif choice == '3':
            self.debug_model()  # Chama o método de depuração
        elif choice == '4':
            self.auto_adjust_model()  # Chama o método de autoajuste
        elif choice == '5':
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
        self.debugger.log_inference(new_data, result)  # Registra a inferência no log
        self.show_menu()  # Retorna ao menu principal

    # Método para treinar o modelo
    def train_model(self):
        print("Training model...")  # Informa que o treinamento está em andamento
        data = np.random.random((100, self.input_shape))  # Simula a criação de dados de treinamento
        labels = np.random.randint(2, size=100)  # Simula a criação de rótulos de treinamento
        self.model.fit(data, labels, epochs=10)  # Treina o modelo com os dados simulados
        print("Model trained successfully.")  # Informa que o treinamento foi concluído
        self.show_menu()  # Retorna ao menu principal

    # Método para iniciar o processo de depuração
    def debug_model(self):
        print("Starting debugger...")  # Informa que a depuração está iniciando
        self.debugger.debug_function(self.run_inference)  # Depura o método de inferência
        self.show_menu()  # Retorna ao menu principal

    # Método para iniciar o autoajuste do modelo
    def auto_adjust_model(self):
        print("Auto-adjusting model...")  # Informa que o autoajuste está em andamento
        new_data = np.random.random((50, self.input_shape))  # Simula novos dados de entrada
        new_labels = np.random.randint(2, size=50)  # Simula novos rótulos de entrada
        self.self_adjuster.update_data_buffer(new_data, new_labels)  # Atualiza o buffer de dados do autoajustador
        self.self_adjuster.auto_adjust()  # Inicia o processo de autoajuste
        self.show_menu()  # Retorna ao menu principal

# Exemplo de uso do sistema
if __name__ == "__main__":
    from tensorflow.keras.models import Sequential  # Importa a classe Sequential do Keras
    from tensorflow.keras.layers import Dense  # Importa a camada Dense do Keras

    input_shape = 10  # Define o formato de entrada para o modelo
    model = Sequential([  # Criação de um modelo sequencial de exemplo
        Dense(64, activation='relu', input_shape=(input_shape,)),  # Primeira camada densa com 64 neurônios
        Dense(1, activation='sigmoid')  # Camada de saída com 1 neurônio, ativação sigmoide
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])  # Compilação do modelo

    protection_system = NeuralProtectionSystem(model, input_shape)  # Inicializa o sistema de proteção
    protection_system.show_menu()  # Exibe o menu do sistema