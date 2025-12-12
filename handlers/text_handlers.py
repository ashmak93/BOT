from aiogram import Router, types
from aiogram.filters import Command
from services.ai_service import AIService

router = Router()
ai = AIService()

main_keyboard = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text="Эмоции"), types.KeyboardButton(text="Главная мысль")],
        [types.KeyboardButton(text="Ответ"), types.KeyboardButton(text="Проверить грамматику")]
    ],
    resize_keyboard=True
)

user_last_text = {}

@router.message(lambda message: message.text in ["Эмоции", "Главная мысль", "Ответ", "Проверить грамматику"])
async def handle_menu_buttons(message: types.Message):
    """Обработка кнопок меню"""
    user_id = message.from_user.id

    if user_id not in user_last_text or not user_last_text[user_id]:
        await message.answer("Сначала отправьте текст для анализа")
        return

    text = user_last_text[user_id]

    if message.text == "Эмоции":
        result = ai.analyze_emotion(text)
    elif message.text == "Главная мысль":
        result = ai.get_main_idea(text)
    elif message.text == "Ответ":
        result = ai.generate_response(text)
    elif message.text == "Проверить грамматику":
        result = ai.check_grammar(text)
    else:
        result = "Неизвестная команда"

    await message.answer(result)


@router.message()
async def handle_text(message: types.Message):
    """Обработка любого текста"""
    text = message.text.strip()
    user_id = message.from_user.id

    if text.startswith('/') or len(text) < 3:
        return

    user_last_text[user_id] = text

    display_text = text[:100] + "..." if len(text) > 100 else text

    await message.answer(
        f"Текст сохранён. Выберите действие на клавиатуре.",
        reply_markup=main_keyboard
    )