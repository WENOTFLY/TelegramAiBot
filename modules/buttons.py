from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def generate_group_buttons(groups):
    """
    Создает кнопки выбора групп для постинга.
    """
    keyboard = InlineKeyboardMarkup(row_width=1)
    for group_id, group_name in groups:
        button = InlineKeyboardButton(text=group_name, callback_data=f"post_group:{group_id}")
        keyboard.add(button)
    return keyboard
