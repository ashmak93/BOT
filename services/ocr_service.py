import pytesseract
from PIL import Image
from services.ocr_service import OCRService
import io

class OCRService:
    @staticmethod
    def extract_text_from_image(image_bytes):
        """Извлекает текст из изображения"""
        try:
            image = Image.open(io.BytesIO(image_bytes))
            text = pytesseract.image_to_string(image, lang='rus+eng')
            return text.strip() if text else "Текст не найден"
        except Exception as e:
            return f"Ошибка обработки: {str(e)}"