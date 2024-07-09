from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer('Это тестовый бот')
