import logging
import asyncio
from aiogram import Bot, Dispatcher

from config import Config
from handlers import start_handlers, text_handlers, photo_handlers

# логирование
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

async def main():
    """Основная функция запуска бота"""
    Config.validate_tokens()

    bot = Bot(token=Config.BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start_handlers.router)
    dp.include_router(photo_handlers.router)
    dp.include_router(text_handlers.router)

    
    logger.info("Бот запускается...")
    
    try:
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        logger.info("Бот остановлен")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
