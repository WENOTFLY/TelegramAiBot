from aiogram import types
from modules.monitoring import get_system_status, monitor_openwebui
from modules.access_control import has_permission

async def view_stats(message: types.Message):
    user_id = message.from_user.id
    if not has_permission(user_id, "view_stats"):
        await message.reply("У вас нет прав на просмотр статистики.")
        return
    
    system_status = get_system_status()
    openwebui_status = monitor_openwebui()

    await message.reply(
        f"📊 Статистика:\n"
        f"CPU Usage: {system_status['cpu_usage']}%\n"
        f"Memory Usage: {system_status['memory_usage']}%\n\n"
        f"OpenWebUI Status: {openwebui_status['status']}\n"
        f"API Latency: {openwebui_status['latency']} сек"
    )
