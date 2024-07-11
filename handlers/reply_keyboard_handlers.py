from aiogram import F, Router
from aiogram.types import Message, FSInputFile
from main import bot

router = Router()
photo_file = FSInputFile('photo.jpg')


@router.message(F.text == 'Адрес')
async def address(message: Message):
    await message.answer('Для перехода на карту кликнете на эту ссылку: '
                         'https://yandex.ru/maps/1104/cherkessk/house/'
                         'prospekt_lenina_1/YEsYdgNoSUUHQFpufX5yc3pqYQ==/'
                         '?ll=42.048001%2C44.232695&z=17')


@router.message(F.text == 'Картинка')
async def picture(message: Message):
    await message.answer('Подождите идет загрузка фото')
    await bot.send_photo(chat_id=message.chat.id, photo=photo_file)

