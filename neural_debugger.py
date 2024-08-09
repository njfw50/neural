import logging  # Importa o módulo de logging para registrar informações detalhadas
import time  # Importa o módulo time para monitoramento de tempo
import sys
import traceback  # Importa o módulo traceback para capturar stack traces

# Classe NeuralDebugger: responsável por registrar e monitorar o sistema
class NeuralDebugger:
    def __init__(self, log_file="neural_debugger.log", log_level=logging.DEBUG):
        self.logger = logging.getLogger("NeuralDebugger")
        self.logger.setLevel(log_level)

        file_handler = logging.FileHandler(log_file)
        console_handler = logging.StreamHandler(sys.stdout)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

        self.start_time = None
        self.logger.info("NeuralDebugger iniciado.")

    # Método para iniciar o monitoramento do tempo de execução de uma operação
    def start_timer(self):
        self.start_time = time.time()  # Armazena o tempo atual
        self.logger.info("Timer iniciado.")  # Registra o início do timer

    # Método para parar o timer e calcular o tempo decorrido
    def stop_timer(self):
        if self.start_time is not None:  # Verifica se o timer foi iniciado
            elapsed_time = time.time() - self.start_time  # Calcula o tempo decorrido
            self.logger.info(f"Tempo de execução: {elapsed_time:.4f} segundos.")  # Registra o tempo de execução
            self.start_time = None  # Reseta o timer
            return elapsed_time  # Retorna o tempo decorrido
        else:
            self.logger.warning("Timer não estava iniciado.")  # Avisa que o timer não estava ativo
            return None  # Retorna None caso o timer não tenha sido iniciado

    # Método para registrar erros ou exceções
    def log_error(self, error_message):
        self.logger.error(f"Erro capturado: {error_message}")  # Registra o erro no log
        self.logger.error("Stack trace:")
        self.logger.error(traceback.format_exc())  # Registra o stack trace completo

    # Método para registrar informações detalhadas sobre o processo de inferência
    def log_inference(self, input_data, output_data, additional_info=None):
        self.logger.info(f"Dados de entrada: {input_data}")
        self.logger.info(f"Resultado da inferência: {output_data}")
        if additional_info:
            self.logger.info(f"Informações adicionais: {additional_info}")
        
    # Método para registrar o estado atual do modelo neural
    def log_model_state(self, model):
        model_summary = []  # Lista para armazenar o resumo do modelo
        model.summary(print_fn=lambda x: model_summary.append(x))  # Gera o resumo do modelo
        self.logger.info("Estado atual do modelo:")  # Inicia o registro do estado do modelo
        for line in model_summary:  # Itera sobre cada linha do resumo
            self.logger.info(line)  # Registra cada linha no log

    # Método para depurar uma função específica
    def debug_function(self, func, *args, **kwargs):
        self.logger.info(f"Iniciando depuração da função: {func.__name__}")  # Registra o início da depuração
        self.start_timer()  # Inicia o timer
        try:
            result = func(*args, **kwargs)  # Executa a função a ser depurada
            self.stop_timer()  # Para o timer após a execução
            self.logger.info(f"Função {func.__name__} executada com sucesso.")  # Registra o sucesso da execução
            return result  # Retorna o resultado da função
        except Exception as e:
            self.log_error(f"Exceção na função {func.__name__}: {str(e)}")  # Registra o erro caso haja exceção
            raise  # Re-levanta a exceção para ser tratada no nível superior
