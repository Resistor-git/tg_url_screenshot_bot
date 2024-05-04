import re
from pathlib import Path
from selenium import webdriver


# УДАЛИ ДЕФОЛТНОЕ ЗНАЧЕНИЕ
async def take_screenshot(url: str = "https://stepik.org/") -> Path:
    """
    Takes a screenshot of the webpage and saves it to a file.
    Returns the path to the saved file.
    """
    screenshots_dir = Path.cwd() / "data" / "screenshots"
    screenshot_path = screenshots_dir / "screenshot.png"

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)

    driver.get(url)

    # current_url = driver.current_url
    # cleaned_url = re.sub(r"[^a-zA-Z0-9]", "_", current_url)

    driver.save_screenshot(screenshot_path)
    # логи: сохранил скриншот с таким то именем

    driver.quit()

    return screenshot_path
