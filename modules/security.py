import os
from dotenv import load_dotenv

load_dotenv()

def get_env_variable(key: str, default=None):
    """
    Получает значение переменной окружения из .env
    """
    return os.getenv(key, default)
