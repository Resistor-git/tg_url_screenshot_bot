import asyncio
import logging
import time

from aiogram import Router, Bot
from aiogram.types import Message, ErrorEvent, InputMediaPhoto, FSInputFile
from selenium.common import WebDriverException

from helpers import take_screenshot, address_formatter, caption_maker
from lexicon import LEXICON_RUS

router_screenshot = Router()

logger = logging.getLogger(__name__)


@router_screenshot.message()
async def process_message_with_url(message: Message) -> None:
    """
    Checks if message from user has an url. If there is the url - sends the message with a screenshot of the webpage.
    :param message: message from the user (built-in aiogram type)
    :return: None
    """
    # url_pattern = r'(?:(?:https?|http):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+'
    #
    # matches = re.findall(url_pattern, message.text)
    # #
    # # if matches:
    # #     # обработать google.com -> str.startswith() hhtps//...
    # #     for match in matches:
    # #         print(match)
    #         # await message.answer(text=LEXICON_RUS["processing"])
    #         # # записать событие в лог
    #         # await take_screenshot(match)
    #         # await message.answer(text='empty done')

    start_time = time.time()
    entities: list = message.entities
    if entities:
        for entity in entities:
            if entity.type == "url":
                address = address_formatter(entity.extract_from(message.text))
                bot_response: Message = await message.answer_photo(
                    photo=FSInputFile("data/loading.gif"),
                    caption=LEXICON_RUS["processing"],
                    reply_to_message_id=message.message_id,
                )
                try:
                    screenshot_path, page_title = await take_screenshot(
                        address, message
                    )
                    end_time = time.time()
                    execution_time = end_time - start_time
                    await bot_response.edit_media(
                        media=InputMediaPhoto(
                            media=FSInputFile(screenshot_path),
                            caption=caption_maker(page_title, address, execution_time),
                        )
                    )
                except WebDriverException:
                    logger.exception(f"Something went wrong. URL: {address}")
                    await asyncio.sleep(5)
                    await bot_response.edit_media(
                        media=InputMediaPhoto(
                            media=FSInputFile("data/sorry.png"),
                            caption=LEXICON_RUS["error"],
                        ),
                    )


# @router_screenshot.error()
# async def error_handler(event: ErrorEvent):
#     # лог
#     pass
