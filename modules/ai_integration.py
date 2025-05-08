import requests
import os
from utils.file_manager import load_json

# Загрузка конфигурации моделей
config = load_json("config/config.json")
models = load_json("config/models.json")["models"]
OPENWEBUI_API_URL = os.getenv("OPENWEBUI_API_URL")

def get_ai_response(user_text: str, model: str = "qwen3:0.6b") -> str:
    """
    Отправляет текст на OpenWebUI API и получает ответ от модели.
    """
    try:
        model_config = models.get(model, models["qwen3:0.6b"])
        response = requests.post(
            f"{OPENWEBUI_API_URL}/api/generate",
            json={
                "prompt": user_text,
                "temperature": model_config["temperature"],
                "max_tokens": model_config["max_tokens"]
            }
        )
        response_data = response.json()
        return response_data.get("response", "Ошибка при обработке запроса ИИ.")
    except Exception as e:
        return f"Ошибка соединения с ИИ: {str(e)}"
