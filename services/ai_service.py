from gigachat import GigaChat
from config import Config

class AIService:
    def __init__(self):
        self.giga = GigaChat(credentials=Config.GIGACHAT_TOKEN, verify_ssl_certs=False)
    
    def analyze_emotion(self, text: str) -> str:
        """Анализ эмоциональной окраски текста"""
        prompt = f"""Определи эмоциональную окраску этого текста. Ответь кратко, одним-двумя-тремя словами, только ответ, без "вот ваш ответ:".
        
        Текст: "{text}" """
        
        try:
            response = self.giga.chat(prompt)
            return f"Эмоциональная окраска:\n\n{response.choices[0].message.content}"
        except Exception as e:
            return f"Ошибка: {str(e)}"
    
    def get_main_idea(self, text: str) -> str:
        """Выделение главной мысли текста"""
        prompt = f"""Выдели главную мысль этого текста. Ответь кратко, 1-2 предложениями, БЕЗ "главная мысль:".
        
        Текст: "{text}" """
        
        try:
            response = self.giga.chat(prompt)
            return f"Главная мысль:\n\n{response.choices[0].message.content}"
        except Exception as e:
            return f"Ошибка: {str(e)}"
    
    def generate_response(self, text: str) -> str:
        """Генерация ответа на текст"""
        prompt = f"""Сгенерируй вежливый, уместный и короткий ответ на это сообщение от лица того, кому прислали сообщение.
        
        Сообщение: "{text}" """
        
        try:
            response = self.giga.chat(prompt)
            return f"Ответ:\n\n{response.choices[0].message.content}"
        except Exception as e:
            return f"Ошибка: {str(e)}"
    
    def check_grammar(self, text: str) -> str:
        """Проверка грамматики и пунктуации"""
        prompt = f"""Проверь этот текст на грамматические и пунктуационные ошибки. 
        Исправь ошибки и верни только исправленный текст без форматирования.
        
        Текст: "{text}" """
        
        try:
            response = self.giga.chat(prompt)
            return f"Результат проверки:\n\n{response.choices[0].message.content}"
        except Exception as e:
            return f"Ошибка: {str(e)}"
