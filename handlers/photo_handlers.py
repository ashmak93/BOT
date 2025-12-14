from aiogram import Router, types
from aiogram.filters import Command
from services.ocr_service import OCRService
import logging
import io

router = Router()
logger = logging.getLogger(__name__)

@router.message(lambda message: message.photo is not None)
async def handle_image(message: types.Message):
    """Обрабатывает изображение и отправляет распознанный текст"""
    try:
        photo = message.photo

        photo_file = await photo.download(destination=io.BytesIO())
        image_bytes = photo_file.getvalue()

        text = OCRService.extract_text_from_image(image_bytes)

        await message.answer(f"Распознанный текст:\n\n{text}")

    except Exception as e:
        logger.error(f"Ошибка при обработке: {e}", exc_info=True)
        await message.answer(f"Произошла ошибка при обработке изображения: {str(e)}")