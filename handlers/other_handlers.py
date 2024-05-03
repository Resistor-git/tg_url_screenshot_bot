from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from lexicon import LEXICON_RUS

router_other = Router()


@router_other.message(CommandStart())
async def start_command(message: Message):
    await message.answer(text=LEXICON_RUS["start"])


@router_other.message(Command(commands="help"))
async def help_command(message: Message):
    await message.answer(text=LEXICON_RUS["help"])
