import logging
import os
from datetime import datetime

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, f"bot_{datetime.now().strftime('%Y-%m-%d')}.log")

def setup_logging():
    """
    Настраивает систему логирования.
    """
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE, encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
    logging.info("Logging system initialized.")

def log_user_action(user_id: int, action: str, details: str = ""):
    """
    Записывает действия пользователя в лог.
    """
    logging.info(f"User {user_id} performed action: {action}. {details}")

def log_error(error: str, details: str = ""):
    """
    Записывает ошибки в лог.
    """
    logging.error(f"Error: {error}. {details}")
