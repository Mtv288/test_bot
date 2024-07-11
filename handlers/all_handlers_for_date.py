from aiogram import Router
from aiogram.types import Message
import datetime

router = Router()


@router.message()
async def data_info(message: Message):
    try:
        datetime.datetime.strptime(message.text, '%d.%m.%Y')
        await message.answer('Формат даты верен')
    except ValueError:
        await message.answer('Формат даты не верен')



