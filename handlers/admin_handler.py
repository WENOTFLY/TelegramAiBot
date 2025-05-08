from aiogram import types
from modules.access_control import has_permission

async def admin(message: types.Message):
    user_id = message.from_user.id
    if not has_permission(user_id, "manage_users"):
        await message.reply("У вас нет прав на выполнение административных команд.")
        return
    
    await message.reply(
        "Панель администратора:\n"
        "/stats - Просмотр статистики\n"
        "/roles - Управление ролями\n"
        "/logs - Просмотр логов"
    )
