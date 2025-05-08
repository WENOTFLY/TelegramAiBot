from aiogram import types
from modules.user_interaction import set_user_language, get_start_message

async def change_language(message: types.Message):
    user_id = message.from_user.id
    if message.text == "🇬🇧 English":
        set_user_language(user_id, "en")
        await message.answer("Language set to English.")
    elif message.text == "🇷🇺 Русский":
        set_user_language(user_id, "ru")
        await message.answer("Язык установлен на русский.")
    
    welcome_message = get_start_message(user_id)
    await message.answer(welcome_message)
