import logging
from pathlib import Path

from selenium import webdriver

logger = logging.getLogger(__name__)


# @measure_execution_time
async def take_screenshot(url: str) -> Path:
    """
    Takes a screenshot of the webpage and saves it to a file.
    Returns the path to the saved file.
    """
    screenshots_dir = Path.cwd() / "data" / "screenshots"
    screenshot_path = (
        screenshots_dir / "screenshot.png"
    )  # вот здесь вызов функции называлки

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
