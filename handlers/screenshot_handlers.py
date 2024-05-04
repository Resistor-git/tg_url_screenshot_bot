from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
###
import re
from pathlib import Path
from selenium import webdriver
###
from lexicon import LEXICON_RUS

router_screenshot = Router()


async def test_screenshot():
    # перенести в helpers или типа того
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
    driver.get("https://stepik.org/")

    current_url = driver.current_url
    cleaned_url = re.sub(r"[^a-zA-Z0-9]", "_", current_url)

    # driver.save_screenshot(f"{cleaned_url}.png")
    driver.save_screenshot(f"tst_scrnshot.png")

    driver.quit()
    # path_screenshot = Path("tst_scrnshot.png")


@router_screenshot.message(Command(commands="test"))
async def test_command(message: Message):
    await message.answer(text=LEXICON_RUS["processing"])
    # записать событие в лог
    await test_screenshot()
    await message.answer(text='tst done')
