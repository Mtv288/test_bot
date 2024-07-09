from aiogram import Bot, Dispatcher
import asyncio
from dotenv import load_dotenv
import os
from handlers import command
import logging

load_dotenv()
bot = Bot(os.getenv('TOKEN'))


async def start():
    logging.basicConfig(filename='logs.log', level=logging.ERROR)
    dp = Dispatcher()
    dp.include_router(command.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start())
