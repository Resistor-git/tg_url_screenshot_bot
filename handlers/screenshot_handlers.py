import asyncio
import logging
import time

from aiogram import Router
from aiogram.exceptions import TelegramNetworkError
from aiogram.types import Message, InputMediaPhoto, FSInputFile
from selenium.common import WebDriverException, TimeoutException

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
                    screenshot_task = asyncio.create_task(
                        take_screenshot(address, message)
                    )
                    screenshot_path, page_title = await screenshot_task
                    end_time = time.time()
                    execution_time = end_time - start_time
                    await bot_response.edit_media(
                        media=InputMediaPhoto(
                            media=FSInputFile(screenshot_path),
                            caption=caption_maker(page_title, address, execution_time),
                        )
                    )
                except (WebDriverException, TelegramNetworkError):
                    logger.exception(f"Something went wrong. URL: {address}")
                    await bot_response.edit_media(
                        media=InputMediaPhoto(
                            media=FSInputFile("data/sorry.png"),
                            caption=LEXICON_RUS["error"],
                        ),
                    )
                except TimeoutException:
                    logger.exception(f"No response from site. URL: {address}")
                    await bot_response.edit_media(
                        media=InputMediaPhoto(
                            media=FSInputFile("data/sorry.png"),
                            caption=LEXICON_RUS["error_no_response"],
                        ),
                    )
