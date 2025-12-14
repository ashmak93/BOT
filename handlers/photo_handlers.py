from aiogram import Router, types, Dispatcher
from aiogram.types import ContentType
import pytesseract
from PIL import Image
import io

router = Router()

@router.message()
async def handle_image(message: types.Message):
    """Обрабатывает загруженное изображение и отправляет распознанный текст"""
    if not message.photo:
        return

    try:
        photo = message.photo[-1]

        photo_file = await photo.download(destination=io.BytesIO())
        image_bytes = photo_file.getvalue()

        image = Image.open(io.BytesIO(image_bytes))
        text = pytesseract.image_to_string(image, lang='rus+eng')

        cleaned_text = text.strip()

        if cleaned_text:
            await message.reply(f"Распознанный текст:\n\n{cleaned_text}")
        else:
            await message.reply("Не удалось распознать текст с изображения")

    except Exception as e:
        await message.reply(f"Ошибка при обработке: {str(e)}")