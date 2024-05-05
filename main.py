import asyncio
import logging

from aiogram import Bot, Dispatcher

# from aiogram.client.default import DefaultBotProperties
# from aiogram.enums import ParseMode

from config_data.config import Config, load_config
from handlers import router_screenshot, router_other

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s",
    )
    logger.info("Bot launch")

    config: Config = (
        load_config()
    )  # адрес env фала можно не указывать, библиотека сама ищет

    # объект хранилища, чтобы хранить данные о пользователе в Redis
    # storage = ...

    bot = Bot(
        token=config.tg_bot.bot_token,
        # default=DefaultBotProperties(parse_mode=ParseMode.HTML)  # дефолтные настройки, см исходники
    )
    dispatcher = Dispatcher()
    # dispatcher = Dispatcher(storage=storage)
    # dispatcher.workflow_data.update()  # всякие дополнительные данные
    # порядок регистрации роутеров имеет значение
    dispatcher.include_router(router_other)
    dispatcher.include_router(router_screenshot)

    # await set_main_menu(bot)
    # await bot.delete_webhook(drop_pending_updates=True)  # пропуск накопившихся апдейтов - не нужен?
    await dispatcher.start_polling(bot)


asyncio.run(main())
