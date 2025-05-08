import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from handlers.start_handler import start
from handlers.post_handler import generate_post, receive_topic, post_to_group
from handlers.admin_handler import admin
from handlers.stats_handler import view_stats
from handlers.error_handler import handle_error
from handlers.roles_handler import list_roles, add_role
from handlers.language_handler import change_language

from modules.logging_handler import setup_logging, log_user_action, log_error
from utils.file_manager import load_json

# Загрузка переменных окружения
load_dotenv()

# Настройка логирования
setup_logging()
logger = logging.getLogger(__name__)

# Инициализация бота и диспетчера с FSM
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = Bot(token=TELEGRAM_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Подключение обработчиков
dp.register_message_handler(start, commands=["start"])
dp.register_message_handler(generate_post, commands=["generate_post"])
dp.register_message_handler(receive_topic, state="PostGeneration:waiting_for_topic")
dp.register_callback_query_handler(post_to_group, lambda call: call.data.startswith("post_group"), state="PostGeneration:waiting_for_group")

dp.register_message_handler(admin, commands=["admin"])
dp.register_message_handler(view_stats, commands=["stats"])
dp.register_message_handler(list_roles, commands=["roles"])
dp.register_message_handler(add_role, commands=["add_role"])
dp.register_message_handler(change_language, lambda message: message.text in ["🇬🇧 English", "🇷🇺 Русский"])

# Обработчик ошибок
async def on_error(update, exception):
    log_error(str(exception), f"Occurred in update: {update}")
    if isinstance(update, types.Message):
        await update.reply("Произошла ошибка. Попробуйте позже.")

dp.register_errors_handler(on_error)

logger.info("Bot is starting...")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
