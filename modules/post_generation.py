from modules.ai_integration import get_ai_response
from utils.file_manager import load_json

def generate_post(topic: str, model: str = "qwen3:0.6b") -> str:
    """
    Генерирует текст поста на заданную тему.
    """
    prompt = f"Напиши информативный и интересный пост на тему: {topic}."
    return get_ai_response(prompt, model)

def get_available_groups():
    """
    Возвращает список доступных групп для постинга.
    """
    groups = load_json("config/groups.json").get("groups", [])
    return [(group["id"], group["name"]) for group in groups]
