from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    bot_token: str
    # admins_ids: list[int] | None = None  # is None valid???


@dataclass
class Config:
    tg_bot: TgBot
    # admins_ids =


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            bot_token=env("BOT_TOKEN"),
            # admin_ids=list(map(int, env.list('ADMIN_IDS')))
        ),
    )
