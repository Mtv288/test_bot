from aiogram import Bot, Dispatcher
import asyncio
from dotenv import load_dotenv

bot = ('')


async def srart():
    dp = Dispatcher
    await dp.start_polling(bot)


if __name__ == '__main__':
    start()
