import logging.handlers
import time

from aiogram import Router, F
from aiogram.exceptions import TelegramNetworkError
from aiogram.types import (
    Message,
    InputMediaPhoto,
    FSInputFile,
    CallbackQuery,
    MessageEntity,
)
from selenium.common import WebDriverException, TimeoutException

from helpers import take_screenshot, address_formatter, caption_maker, get_whois
from keyboards import keyboard_more
from lexicon import LEXICON_RUS

router_screenshot = Router()

logger = logging.getLogger(__name__)

formatter = logging.Formatter(
    "%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s\n"
    "---------------------------------------------------------"
)
file_handler = logging.handlers.RotatingFileHandler(
    "logs/general.log", encoding="utf-8", maxBytes=1 * 1024 * 1024, backupCount=2
)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


@router_screenshot.message()
async def process_message_with_url(message: Message) -> None:
    """
    Checks if message from user has an url. If there is the url - sends the message with a screenshot of the webpage.
    :param message: message from the user (built-in aiogram type)
    :return: None
    """
    start_time: float = time.time()
    entities: list[MessageEntity] = message.entities
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
                    end_time: float = time.time()
                    execution_time: float = end_time - start_time
                    await bot_response.edit_media(
                        media=InputMediaPhoto(
                            media=FSInputFile(screenshot_path),
                            caption=caption_maker(page_title, address, execution_time),
                        ),
                        reply_markup=keyboard_more,
                    )
                except (WebDriverException, TelegramNetworkError):
                    logger.exception(f"Something went wrong. URL: {address}")
                    await bot_response.edit_media(
                        media=InputMediaPhoto(
                            media=FSInputFile("data/sorry.png"),
                            caption=LEXICON_RUS["error_generic"],
                        )
                    )
                except TimeoutException:
                    logger.exception(f"No response from site. URL: {address}")
                    await bot_response.edit_media(
                        media=InputMediaPhoto(
                            media=FSInputFile("data/sorry.png"),
                            caption=LEXICON_RUS["error_no_response"],
                        )
                    )


@router_screenshot.callback_query(F.data == "button_more_press")
async def process_button_more_press(callback: CallbackQuery) -> None:
    """
    Shows alert message with information about domain.
    Url (domain) is taken from the quoted message.
    Info is provided by function get_whois()
    :param callback:
    :return:
    """
    message: Message = callback.message.reply_to_message
    entities: list[MessageEntity] = message.entities
    url = LEXICON_RUS["no_whois"]
    for entity in entities:
        if entity.type == "url":
            url = entity.extract_from(message.text)
    await callback.answer(text=get_whois(url), show_alert=True)
