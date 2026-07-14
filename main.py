import sys
import os

# Ensure the src directory is in the python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.ui.cli import NeuralCLI

if __name__ == "__main__":
    """
    Main entrypoint for the Neural System.
    """
    cli = NeuralCLI()
    cli.run()
