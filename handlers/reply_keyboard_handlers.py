from aiogram import F, Router, Bot, types
from aiogram.types import Message, InputFile, input_media

router = Router()


@router.message(F.text == 'Адрес')
async def adress(message: Message):
    await message.answer('https://yandex.ru/maps/1104/cherkessk/house/'
                         'prospekt_lenina_1/YEsYdgNoSUUHQFpufX5yc3pqYQ==/?ll=42.048001%2C44.232695&z=17')
