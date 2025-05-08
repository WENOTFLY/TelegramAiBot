from aiogram import types
from modules.access_control import has_permission
from utils.file_manager import load_json, save_json

async def list_roles(message: types.Message):
    user_id = message.from_user.id
    if not has_permission(user_id, "manage_roles"):
        await message.reply("У вас нет прав на управление ролями.")
        return
    
    permissions = load_json("config/permissions.json")
    roles = permissions.get("roles", {})
    
    roles_text = "📋 Доступные роли:\n"
    for role, details in roles.items():
        roles_text += f"🔹 {role}:\n - " + "\n - ".join(details["permissions"]) + "\n\n"
    
    await message.reply(roles_text)

async def add_role(message: types.Message):
    user_id = message.from_user.id
    if not has_permission(user_id, "manage_roles"):
        await message.reply("У вас нет прав на управление ролями.")
        return

    parts = message.text.split()
    if len(parts) < 3:
        await message.reply("Используйте: /add_role [user_id] [role]")
        return

    target_id = parts[1]
    role = parts[2]

    permissions = load_json("config/permissions.json")
    if role not in permissions["roles"]:
        await message.reply("Такой роли не существует.")
        return
    
    user_roles = permissions["users"].get(target_id, {}).get("roles", [])
    if role not in user_roles:
        user_roles.append(role)
        permissions["users"][target_id] = {"roles": user_roles}
        save_json("config/permissions.json", permissions)
        await message.reply(f"Роль {role} добавлена пользователю {target_id}.")
    else:
        await message.reply("Пользователь уже имеет эту роль.")
