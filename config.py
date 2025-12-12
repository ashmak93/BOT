import os

class Config:
    BOT_TOKEN = None
    GIGACHAT_TOKEN = None
    
    if os.path.exists("tokens.txt"):
        with open("tokens.txt", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("BOT_TOKEN="):
                    BOT_TOKEN = line.split("=", 1)[1].strip()
                elif line.startswith("GIGACHAT_TOKEN="):
                    GIGACHAT_TOKEN = line.split("=", 1)[1].strip()
    
    @classmethod
    def validate_tokens(cls):
        """Проверка наличия токенов"""
        if not cls.BOT_TOKEN:
            raise ValueError("BOT_TOKEN не найден. Проверьте tokens.txt файл")
        if not cls.GIGACHAT_TOKEN:
            raise ValueError("GIGACHAT_TOKEN не найден. Зарегистрируйтесь на developers.sber.ru")
        print("Все токены загружены из tokens.txt")
        return True