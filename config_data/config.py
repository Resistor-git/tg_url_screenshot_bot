from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    bot_token: str


# @dataclass
# class DbConnection:
#     db_name: str
#     db_user: str
#     db_password: str
#     db_host: str
#     db_port: str


@dataclass
class Config:
    tg_bot: TgBot
    # db_connection: DbConnection


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            bot_token=env("BOT_TOKEN"),
        ),
        # db_connection=DbConnection(
        #     db_name=env("POSTGRES_DB"),
        #     db_user=env("POSTGRES_USER"),
        #     db_password=env("POSTGRES_PASSWORD"),
        #     db_host=env("POSTGRES_HOST"),
        #     db_port=env("POSTGRES_PORT"),
        # ),
    )
