import logging
import os

def setup_logging():
    """
    Настраивает систему логирования.
    """
    logging_level = os.getenv("LOGGING_LEVEL", "INFO")
    logging.basicConfig(level=logging_level, 
                        format="%(asctime)s - %(levelname)s - %(message)s",
                        handlers=[
                            logging.FileHandler("logs/bot.log"),
                            logging.StreamHandler()
                        ])
