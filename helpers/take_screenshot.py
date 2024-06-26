import re
import logging.handlers
from pathlib import Path

from aiogram.types import Message
from selenium import webdriver

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


def address_formatter(url: str) -> str:
    """
    Formats the url, so it looks like https://something.com or http://something.com
    :param url: string, result of entity.extract_from aiogram method
    :return: string formatted like https://something.com or http://something.com
    """
    if url.lower().startswith("https://") or url.lower().startswith("http://"):
        return url.lower()
    formatted_url: str = "https://" + url.lower()
    return formatted_url


def caption_maker(page_title: str, url: str, execution_time: float):
    """
    Creates a caption to the message with screenshot.
    :param page_title: title of the webpage from user prompt, extracted by take_screenshot()
    :param url: formatted address from address_formatter()
    :param execution_time: duration from user prompt till bot sending a screenshot
    :return: formatted string
    """
    return (
        f"{page_title}\n\nВеб-сайт: {url}\nВремя обработки: {execution_time:.2f} секунд"
    )


def name_file(url: str, message: Message) -> str:
    """
    Generates the name for screenshot.
    :param url: string, formatted like https://something.com
    :param message: object of the telegram message
    :return: string with date, time, user_id and two levels of domain
    """
    date_time: str = message.date.strftime("%y-%m-%d-%H-%M-%S")
    user_id: str = str(message.from_user.id)  # если в канале, то пустое?
    domain: str = re.search(r"(?<=://)([^/]+)", url).group(1).replace(".", "-")
    return "_".join((date_time, user_id, domain)) + ".png"


async def take_screenshot(url: str, message: Message) -> tuple[Path, str]:
    """
    Takes a screenshot of the webpage and saves it to a png file.
    Filename is generated by function name_file()
    Provides additional info about the page: title.
    Returns the path to the saved file and title of the page.
    :param url: string, result of entity.extract_from aiogram method
    :param message: object of the telegram message
    :return: None
    """
    screenshots_dir = Path.cwd() / "data" / "screenshots"
    filename = name_file(url, message)
    screenshot_path = screenshots_dir / filename

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    driver.set_page_load_timeout(30)
    page_title = driver.title
    driver.save_screenshot(screenshot_path)
    driver.quit()

    logger.info(f"Saved screenshot. Filename: {screenshot_path.name} URL: {url}")

    return screenshot_path, page_title
