from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from modules.post_generation import generate_post, get_available_groups
from modules.buttons import generate_group_buttons
from modules.access_control import has_permission
from modules.logging_handler import log_user_action

class PostGeneration(StatesGroup):
    waiting_for_topic = State()
    waiting_for_group = State()

async def generate_post(message: types.Message):
    user_id = message.from_user.id
    log_user_action(user_id, "Attempted to generate a post")

    if not has_permission(user_id, "generate_post"):
        await message.reply("У вас нет прав на создание поста.")
        log_user_action(user_id, "Access denied to generate post")
        return
    
    await message.reply("Введите тему поста:")
    await PostGeneration.waiting_for_topic.set()

async def receive_topic(message: types.Message, state: FSMContext):
    topic = message.text
    user_id = message.from_user.id
    await state.update_data(topic=topic)
    log_user_action(user_id, "Entered topic for post generation", topic)
    
    groups = get_available_groups()
    keyboard = generate_group_buttons(groups)
    await message.reply("Выберите группу для постинга:", reply_markup=keyboard)
    await PostGeneration.waiting_for_group.set()

async def post_to_group(callback_query: types.CallbackQuery, state: FSMContext):
    group_id = int(callback_query.data.split(":")[1])
    user_data = await state.get_data()
    topic = user_data.get("topic")
    user_id = callback_query.from_user.id

    generated_text = generate_post(topic)
    await callback_query.bot.send_message(group_id, generated_text)
    await callback_query.message.answer(f"Пост опубликован в группу (ID: {group_id}).")
    log_user_action(user_id, "Posted generated text", f"Group ID: {group_id}")
    await state.finish()
