from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_kb():
    address = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Адрес')
            ], [
                KeyboardButton(text='Картинка')
            ]
        ], resize_keyboard=True
    )
    return address


