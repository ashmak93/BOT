import pytesseract
from PIL import Image
import io

class OCRService:
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        pass
    
    def extract_text_from_image(self, image_bytes: bytes) -> str:
        """Извлечение текста из изображения"""
        try:
            # Открываем изображение
            image = Image.open(io.BytesIO(image_bytes))
            
            # Улучшаем контраст для лучшего распознавания
            image = image.convert('L')  # Черно-белое
            # image = image.point(lambda x: 0 if x < 128 else 255)  # Бинаризация
            
            # Распознаем текст (русский + английский)
            text = pytesseract.image_to_string(image, lang='rus+eng')
            
            # Проверяем результат
            if not text or text.isspace():
                return "Текст не найден на изображении"
            
            return text.strip()
            
        except Exception as e:
            return f"Ошибка распознавания: {str(e)}"
