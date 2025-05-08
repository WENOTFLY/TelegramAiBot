import json
from utils.file_manager import load_json, save_json

memory_file = "config/memory.json"

def get_user_memory(user_id: int):
    """
    Возвращает память пользователя.
    """
    memory = load_json(memory_file)
    return memory.get(str(user_id), {})

def save_user_memory(user_id: int, data: dict):
    """
    Сохраняет память пользователя.
    """
    memory = load_json(memory_file)
    memory[str(user_id)] = data
    save_json(memory_file, memory)

def clear_user_memory(user_id: int):
    """
    Очищает память пользователя.
    """
    memory = load_json(memory_file)
    if str(user_id) in memory:
        del memory[str(user_id)]
        save_json(memory_file, memory)
