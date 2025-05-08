import logging
from aiogram import types

logger = logging.getLogger(__name__)

async def handle_error(update: types.Update, exception):
    """
    Обработчик ошибок. Записывает ошибки в лог.
    """
    logger.error(f"Ошибка: {exception}")
    if isinstance(update, types.Message):
        await update.reply("Произошла ошибка. Попробуйте позже.")
