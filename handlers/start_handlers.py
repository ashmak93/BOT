from aiogram import Router, types
from aiogram.filters import CommandStart, Command

router = Router()

@router.message(CommandStart())
async def start_command(message: types.Message):
    """Обработчик команды /start и клавиатура"""
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="Эмоции")],
            [types.KeyboardButton(text="Главная мысль")],
            [types.KeyboardButton(text="Ответ")],
            [types.KeyboardButton(text="Проверить грамматику")],
        ],
        resize_keyboard=True
    )
    
    await message.answer(
        "*Бот для анализа и работы с текстом*\n\n"
        "*Что умею:*\n"
        "• Анализировать эмоции в тексте\n"
        "• Выделять главную мысль\n"
        "• Генерировать ответы\n"
        "• Проверять грамматику\n"
        "• Читать текст с картинок\n\n"
        "Отправьте текст или картинку!",
        parse_mode="Markdown",
        reply_markup=keyboard
    )

@router.message(Command("help"))
async def help_command(message: types.Message):
    """Обработчик команды /help"""
    await message.answer(
        "*Помощь*\n\n"
        "*Как использовать:*\n"
        "1. Отправьте текст или картинку/скриншот с текстом\n"
        "2. Выберите действие из меню\n\n"
        "*Команды:*\n"
        "/start - начать работу\n"
        "/help - эта справка",
        parse_mode="Markdown"
    )
