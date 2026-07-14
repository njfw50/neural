import logging
import os

class CanonicalLogger:
    """
    Canon X - Infrastructure Layer: Logging and external persistence.
    Follows Canon V (Book of Life) principles.
    """
    def __init__(self, log_name="neural_system"):
        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(logging.INFO)
        if not self.logger.handlers:
            ch = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            ch.setFormatter(formatter)
            self.logger.addHandler(ch)

    def info(self, message):
        self.logger.info(message)

    def log_event(self, event_type, details):
        # Placeholder for Book of Life integration
        self.info(f"EVENT [{event_type}]: {details}")
