from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_kb():
    main = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Адрес')
            ]
        ], resize_keyboard=True
    )
    return main
