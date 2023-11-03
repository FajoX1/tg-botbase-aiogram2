from aiogram import types

async def start_kb(user_id):
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    keyboard.add(
       types.InlineKeyboardButton(text='💻 Repository', url='https://github.com/fajox1/tg-botbase-aiogram2'),
    )

    return keyboard