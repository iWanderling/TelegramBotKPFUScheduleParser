""" Скрипт, реализующий парсинг таблицы с расписанием и перенос обновлённой таблицы в Google Sheets """

# Основные функции программы. Импорты записаны в порядке их использования:
from functions.creds_creator import creds_create  # Создание JSON-файла [Credentials.json]
from functions.separator import separate_merges  # Разделение объединённых ячеек таблицы
from functions.parser import parsing  # Парсинг таблицы
from functions.gsheets import gs_transfer  # Загрузка таблицы с сервера в Google Sheets


# Зависимости:
from constant import SLEEP_TIME, LINKS  # Переменная, обозначающая время перерыва и список ссылок на загрузку таблиц
from dotenv import load_dotenv  # Загрузка переменных сред
from logging import getLogger  # Создание логирования
from threading import Thread  # Добавление многопоточности
from urllib import request  # Загрузка таблицы
from requests import get  # Посылка GET-запроса на сайт проекта для его непрерывной работы
from flask import Flask  # Создание ВЕБ-сервера
from time import sleep  # Функция для создания перерыва работы программы
import os  # Получение переменных сред


# Инициализация лога, приложения Flask, загрузка переменных сред и
# создание таблицы Credentials.json ("creds.json"):
logger = getLogger(__name__)
app = Flask(__name__)
load_dotenv()
# creds_create()


# Функция, запускающая приложение Flask (ВЕБ-сервер):
def run_application():
    app.run(host="0.0.0.0", port=5000)  # port = os.getenv("PORT")


# Главная страница сайта ВЕБ-сервера:
@app.route('/')
def hello_world():
    return 'Wake Up! You must work!'


# Функция, выполняющая скрипт - парсинг:
def do_script() -> None:
    for i in range(4):
        # Загрузка таблицы:
        request.urlretrieve(LINKS[i], f"tables/{i + 1}/RawTable.xlsx")

        # Программа реализуется за счёт последовательной работы трёх функций:
        separate_merges(f"tables/{i + 1}/RawTable.xlsx", f"tables/{i + 1}/PreparedTable.xlsx")
        parsing(f"tables/{i + 1}/PreparedTable.xlsx", f"tables/{i + 1}/CookedTable.xlsx", i)
        gs_transfer(f"tables/{i + 1}/CookedTable.xlsx", i + 1)


# Работа программы:
if __name__ == "__main__":
    # Создание отдельного потока для работы ВЕБ-сервера и его запуск:
    flask_thread = Thread(target=run_application)
    flask_thread.start()

    # Цикл, выполняющий скрипт с периодичностью SLEEP_TIME (в секундах):
    while True:
        try:
            logger.warning("Starting to do script...")
            do_script()  # Выполнение скрипта
            logger.warning("✔️ Table updates successfully... ✔️")

            # Посылка GET-запроса (будим засыпающий хостинг):
            req = get("https://telegrambotkpfuscheduleparser.onrender.com")
            logger.warning("✔️ Request has done... ✔️")

            # Перерыв:
            sleep(SLEEP_TIME)
        except Exception as e:
            logger.warning(f"❌ ERROR: {e} ❌")
