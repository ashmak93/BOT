import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    GIGACHAT_TOKEN = os.getenv("GIGACHAT_TOKEN")
    
    @classmethod
    def validate_tokens(cls):
        """Проверка наличия токенов"""
        if not cls.BOT_TOKEN:
            raise ValueError("BOT_TOKEN не найден. Проверьте .env файл")
        if not cls.GIGACHAT_TOKEN:
            raise ValueError("GIGACHAT_TOKEN не найден. Зарегистрируйтесь на developers.sber.ru")
        print("Все токены загружены")
        return True
