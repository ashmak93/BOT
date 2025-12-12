from aiogram import Router, types
from services.ocr_service import OCRService
from services.ai_service import AIService

router = Router()
ocr = OCRService()
ai = AIService()

@router.message(lambda message: message.photo)
async def handle_photo(message: types.Message):
    """Обработка фотографий"""
    await message.answer("Читаю текст с картинки...")
    
    try:
        # Берем фото наилучшего качества
        photo = message.photo[-1]
        file = await message.bot.get_file(photo.file_id)
        file_bytes = await message.bot.download_file(file.file_path)
        
        # Распознаем текст
        extracted_text = ocr.extract_text_from_image(file_bytes.read())
        
        # Если текст распознан успешно
        if extracted_text and not extracted_text.startswith("❌"):
            keyboard = types.InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        types.InlineKeyboardButton(text="Проанализировать", 
                                                 callback_data=f"img_em:{extracted_text[:100]}"),
                    ],
                    [
                        types.InlineKeyboardButton(text="Проверить грамматику", 
                                                 callback_data=f"img_gram:{extracted_text[:100]}"),
                    ]
                ]
            )
            
            response = f"Распознанный текст:\n\n{extracted_text[:500]}"
            if len(extracted_text) > 500:
                response += "\n\n... (текст сокращен)"
            
            await message.answer(response, 
                               parse_mode="Markdown", 
                               reply_markup=keyboard)
        else:
            await message.answer("Не удалось распознать текст на изображении")
            
    except Exception as e:
        await message.answer(f"Ошибка обработки фото: {str(e)}")

@router.callback_query(lambda c: c.data.startswith(("img_em:", "img_gram:")))
async def handle_image_callback(callback: types.CallbackQuery):
    """Обработка действий с распознанным текстом"""
    data = callback.data
    text = data.split(":", 1)[1]
    
    await callback.answer("Анализирую...")
    
    if data.startswith("img_em:"):
        result = ai.analyze_emotion(text)
    else:  # img_gram:
        result = ai.check_grammar(text)
    
    await callback.message.answer(result)
