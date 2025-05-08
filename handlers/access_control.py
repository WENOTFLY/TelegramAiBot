from aiogram import types
from modules.access_control import has_permission

async def check_permissions(message: types.Message, permission: str):
    user_id = message.from_user.id
    if not has_permission(user_id, permission):
        await message.reply("У вас нет прав на выполнение этой команды.")
        return False
    return True
