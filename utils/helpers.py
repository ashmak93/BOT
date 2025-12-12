import re

def clean_text(text: str) -> str:
    """Очистка текста от лишних пробелов и символов"""
    if not text:
        return ""
    
    # Убираем лишние пробелы
    text = re.sub(r'\s+', ' ', text)
    
    # Убираем пробелы в начале и конце
    text = text.strip()
    
    return text

def truncate_text(text: str, max_length: int = 2000) -> str:
    """Обрезка текста до максимальной длины"""
    if len(text) <= max_length:
        return text
    
    # Обрезаем и добавляем многоточие
    return text[:max_length-3] + "..."

def format_response(text: str, title: str = "") -> str:
    """Форматирование ответа бота"""
    if title:
        return f"*{title}*\n\n{text}"
    return text
