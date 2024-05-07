# Res Url Screenshot Bot
https://t.me/url_screenshot_bot \
Бот делает скриншот страницы по ссылке предоставленной пользователем.

## Демонстрация работы бота
* Найти бота в telegram: https://t.me/url_screenshot_bot (Res Url Screenshot Bot).
* Нажать `start` или набрать команду `/start`.
* Отправить ссылку на сайт в любом формате. Например: https://www.google.com, http://google.com, www.google.com, google.com.
* Дождаться ответного сообщения со скриншотом.
* Кнопка "Подробнее" под скриншотом показывает информацию о домене.

## Как развернуть бота локально (без Docker)
* Клонировать репозиторий.
* Создать в корне проекта (в папке с файлом `main.py`) файл `.env` и указать `BOT_TOKEN` - токен вашего бота. Образец файла: `.env.example`. Инструкция по получению токена: https://core.telegram.org/bots/tutorial#obtain-your-bot-token
* Установить зависимости из `requirements.txt`: команда `pip install -r requirements.txt`.
* Запустить `main.py`

## Как развернуть бота в Docker контейнере
* Клонировать репозиторий.
* Создать в корне проекта (в папке с файлом `main.py`) файл `.env` и указать `BOT_TOKEN` - токен вашего бота. Образец файла: `.env.example`. Инструкция по получению токена: https://core.telegram.org/bots/tutorial#obtain-your-bot-token
* а) Создать образ и запустить контейнер: в корне проекта выполнить команду `docker compose -f docker-compose-local.yaml up`
* б) Либо скачать образ из docker-hub: `docker compose -f docker-compose-production.yaml up`


## Размещение бота на удалённом сервере
Для переноса бота на удалённый сервер можно воспользоваться GitHub workflow. Файл находится в папке `.github/workflows`.
Он сохраняет код в репозитории GitHub, проверяет код линтером Black, собирает образ и заливает его на docker hub.
Далее происходит подключение к удалённому серверу, копирование файла docker compose с локальной машины и запуск контейнера
на сервере. Обратите внимание, в конце выполняется `docker system prune -f`, что может привести к потере данных.\
Чтобы workflow работал необходимо в вашей копии репозитория указать "секреты":
* DOCKERHUB_USERNAME - логин на docker hub.
* DOCKERHUB_PASSWORD - пароль docker hub.
* HOST - IP адрес удалённого сервера.
* USERNAME - имя пользователя удалённого сервера.
* SSH_KEY - ключ SSH для подключения к удалённому серверу.
* SSH_KEY_PASSPHRASE - пароль от SSH ключа.
Более подробно про "секреты": https://docs.github.com/ru/actions/security-guides/using-secrets-in-github-actions
Более подробно про GitHub Actions workflows: https://docs.github.com/en/actions/using-workflows/about-workflows


## Логи и скриншоты
Бот сохраняет логи в папку `logs`, скриншоты в папку `data/screenshots`. Имя скриншота формируется по шаблону: дата, время, id пользователя telegram, домен.

## Стэк
Python 3.12 \
aiogram 3.5.0 \
selenium 4.20.0 \
python-whois 0.9.4 \
environs 11.0.0

## Известные баги
* Если в одном сообщении пользователя содержится несколько ссылок, то каждый следующий скриншот показывает время обработки всех предыдущих скриншотов вместе взятых. Реальное время обработки не изменяется.
* Если в одном сообщении пользователя содержится несколько ссылок, то кнопка "Подробнее" будет отображать некорректную информацию. 
* Некоторые сайты блокируют IP моего хостера, поэтому бот развёрнутый на моём сервере (https://t.me/url_screenshot_bot) может не отображать часть сайтов. Касается только бота по ссылке, никак не связано с кодом. 


## Автор
[Resistor](https://github.com/Resistor-git/)