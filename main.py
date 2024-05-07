import asyncio
import logging

from aiogram import Bot, Dispatcher

from config_data.config import Config, load_config
from handlers import router_screenshot, router_other

logger = logging.getLogger(__name__)


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s\n"
        "---------------------------------------------------------",
    )
    logger.info("Bot launch")

    config: Config = load_config()

    bot = Bot(
        token=config.tg_bot.bot_token,
    )
    dispatcher = Dispatcher()
    dispatcher.include_router(router_other)
    dispatcher.include_router(router_screenshot)
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
