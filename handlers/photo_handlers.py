from aiogram import Router, types
from aiogram.filters import Command
from services.ocr_service import OCRService
import logging
import io
from aiogram import Bot

router = Router()
logger = logging.getLogger(__name__)


@router.message(lambda message: message.photo)
async def handle_image(message: types.Message, bot: Bot):
    """Обрабатывает изображение и отправляет распознанный текст"""
    try:
        photo = message.photo[-1]
        photo_file = await bot.download(photo.file_id, destination=io.BytesIO())
        image_bytes = photo_file.getvalue()

        text = OCRService.extract_text_from_image(image_bytes)

        from handlers.text_handlers import user_last_text
        user_id = message.from_user.id
        user_last_text[user_id] = text

        from handlers.text_handlers import main_keyboard

        display_text = text

        await message.answer(
            f"Распознанный текст:\n\n{display_text}\n\n"
            f"Теперь выберите тип анализа на клавиатуре.",
            reply_markup=main_keyboard
        )

    except Exception as e:
        await message.answer(f"Ошибка: {str(e)}")