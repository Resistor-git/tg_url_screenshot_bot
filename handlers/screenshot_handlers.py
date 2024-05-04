from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from helpers import take_screenshot
from lexicon import LEXICON_RUS

router_screenshot = Router()


@router_screenshot.message(Command(commands="test"))
async def test_command(message: Message):
    await message.answer(text=LEXICON_RUS["processing"])
    # записать событие в лог
    await take_screenshot()
    await message.answer(text='tst done')
