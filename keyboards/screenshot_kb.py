from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

button_more = InlineKeyboardButton(text="Подробнее", callback_data="button_more_press")
keyboard_more = InlineKeyboardMarkup(inline_keyboard=[[button_more]])
