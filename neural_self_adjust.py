import numpy as np  # Importa NumPy para operações numéricas
from sklearn.model_selection import train_test_split  # Importa função para dividir dados em treinamento e validação
from tensorflow.keras.callbacks import EarlyStopping  # Importa callback de early stopping do Keras

# Classe NeuralSelfAdjust: responsável por ajustar automaticamente o modelo neural
class NeuralSelfAdjust:
    def __init__(self, model, data_buffer_size=1000):
        self.model = model  # Armazena o modelo neural que será ajustado
        self.data_buffer = []  # Buffer para armazenar dados recentes
        self.data_buffer_size = data_buffer_size  # Tamanho máximo do buffer de dados
        self.performance_threshold = 0.8  # Limiar de desempenho aceitável
        self.early_stopping = EarlyStopping(monitor='val_loss', patience=5)  # Early stopping para evitar overfitting

    # Método para atualizar o buffer de dados com novos exemplos
    def update_data_buffer(self, new_data, new_labels):
        for data, label in zip(new_data, new_labels):  # Itera sobre os novos dados e rótulos
            if len(self.data_buffer) >= self.data_buffer_size:
                self.data_buffer.pop(0)  # Remove os dados mais antigos se o buffer estiver cheio
            self.data_buffer.append((data, label))  # Adiciona os novos dados ao buffer

    # Método para avaliar o desempenho atual do modelo
    def evaluate_performance(self, validation_data, validation_labels):
        loss, accuracy = self.model.evaluate(validation_data, validation_labels, verbose=0)  # Avalia o modelo
        return accuracy  # Retorna a acurácia do modelo

    # Método para autoajustar o modelo com base no desempenho
    def auto_adjust(self):
        if len(self.data_buffer) < self.data_buffer_size // 2:
            print("Buffer de dados insuficiente para ajuste.")  # Informa que o buffer não tem dados suficientes
            return  # Sai do método se o buffer estiver muito vazio

        # Extrai dados e rótulos do buffer
        data, labels = zip(*self.data_buffer)  # Separa os dados e rótulos do buffer
        data = np.array(data)  # Converte os dados em array NumPy
        labels = np.array(labels)  # Converte os rótulos em array NumPy

        # Divide os dados em treinamento e validação
        train_data, val_data, train_labels, val_labels = train_test_split(data, labels, test_size=0.2)

        # Avalia o desempenho atual do modelo
        current_performance = self.evaluate_performance(val_data, val_labels)
        print(f"Desempenho atual do modelo: {current_performance:.4f}")

        if current_performance < self.performance_threshold:
            print("Desempenho abaixo do limiar. Iniciando autoajuste do modelo.")

            # Re-treina o modelo com os dados do buffer
            self.model.fit(train_data, train_labels, 
                           validation_data=(val_data, val_labels), 
                           epochs=10, batch_size=32, 
                           callbacks=[self.early_stopping])

            # Reavalia o desempenho após o re-treinamento
            new_performance = self.evaluate_performance(val_data, val_labels)
            print(f"Novo desempenho do modelo após ajuste: {new_performance:.4f}")

            if new_performance < current_performance:
                print("Novo desempenho inferior. Revertendo para o estado anterior.")
                # Aqui você implementaria um mecanismo para recarregar pesos antigos, se necessário.
