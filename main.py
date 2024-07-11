from aiogram import Bot, Dispatcher
import asyncio
from dotenv import load_dotenv
import os
from handlers import command
import logging
from handlers import reply_keyboard_handlers, all_handlers_for_date

load_dotenv()
bot = Bot(os.getenv('TOKEN'))


async def start():
    logging.basicConfig(filename='logs.log', level=logging.ERROR)
    dp = Dispatcher()
    dp.include_router(command.router)
    dp.include_router(reply_keyboard_handlers.router)
    dp.include_router(all_handlers_for_date)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start())
