from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from keyboard.reply_keyboard import main_kb

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer('Это тестовый бот', reply_markup=main_kb())


