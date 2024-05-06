import logging
from pathlib import Path

from aiogram.types import Message
from selenium import webdriver

logger = logging.getLogger(__name__)


def name_file(url: str, message: Message) -> str:
    """
    Generates the name for screenshot.
    :param url:
    :param message:
    :return: string with date, time, user_id and two levels of domain
    """
    date_time: str = message.date.strftime("%y-%m-%d-%H-%M-%S")
    user_id: str = str(message.from_user.id)  # если в канале, то пустое?
    # domain: str = url  # обрезать до something.com
    domain: str = "test-com"
    # здесь вызов нормализатора доменов
    print(date_time, user_id, domain)
    print("_".join((date_time, user_id, domain)))
    return "_".join((date_time, user_id, domain)) + ".png"


async def take_screenshot(url: str, message: Message) -> Path:
    """
    Takes a screenshot of the webpage and saves it to a file. Filename is generated by function name_file()
    Provides additional info about the page: title.
    Returns the path to the saved file and title of the page.
    """
    screenshots_dir = Path.cwd() / "data" / "screenshots"
    filename = name_file(url, message)
    screenshot_path = screenshots_dir / filename

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)

    driver.get(url)

    page_title = driver.title
    # current_url = driver.current_url
    # cleaned_url = re.sub(r"[^a-zA-Z0-9]", "_", current_url)

    driver.save_screenshot(screenshot_path)

    logger.info(f"Saved screenshot. Filename: {screenshot_path.name} URL: {url}")
    # логи: сохранил скриншот с таким то именем

    driver.quit()

    return screenshot_path, page_title


# async def caption_maker(): ...
