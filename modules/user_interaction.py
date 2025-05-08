from utils.file_manager import load_json
from modules.memory import get_user_memory, save_user_memory

messages = load_json("config/messages.json")

def get_start_message(user_id: int) -> str:
    """
    Возвращает приветственное сообщение на языке пользователя.
    """
    user_memory = get_user_memory(user_id)
    user_language = user_memory.get("language", "en")
    return messages["languages"].get(user_language, messages["languages"]["en"])["start_message"]

def set_user_language(user_id: int, language: str):
    """
    Устанавливает язык пользователя и сохраняет в память.
    """
    user_memory = get_user_memory(user_id)
    user_memory["language"] = language
    save_user_memory(user_id, user_memory)
