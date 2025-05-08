from aiogram import types
from modules.user_interaction import get_start_message, set_user_language
from modules.logging_handler import log_user_action

async def start(message: types.Message):
    user_id = message.from_user.id
    set_user_language(user_id, "en")  # По умолчанию английский
    welcome_message = get_start_message(user_id)
    await message.answer(welcome_message)

    log_user_action(user_id, "Started the bot", "User used /start command")

    await message.answer("🌐 Choose your language:\n🇬🇧 English\n🇷🇺 Русский", 
                         reply_markup=types.ReplyKeyboardMarkup(
                             keyboard=[
                                 [types.KeyboardButton("🇬🇧 English")],
                                 [types.KeyboardButton("🇷🇺 Русский")]
                             ], 
                             resize_keyboard=True))
