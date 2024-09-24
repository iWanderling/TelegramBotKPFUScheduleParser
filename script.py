""" Скрипт, реализующий парсинг таблицы с расписанием и перенос обновлённой таблицы в Google Sheets """

# Функции программы
from functions.creds_creator import creds_create
from functions.separator import separate_merges
from functions.gsheets import gs_transfer
from functions.parser import parsing

# Зависимости
from constant import SLEEP_TIME
from dotenv import load_dotenv
from urllib import request
from constant import LINKS
from requests import get
from flask import Flask
from time import sleep
import threading
import logging
import os


# Инициализация лога, приложения Flask, загрузка переменных сред и создание таблицы Credentials.json ("creds.json")
logger = logging.getLogger(__name__)
app = Flask(__name__)
load_dotenv()
# creds_create()


# Функция, запускающая приложение Flask:
def run_application():
    app.run(host="0.0.0.0", port=5000)  # port = os.getenv("PORT")


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
    flask_thread = threading.Thread(target=run_application)
    flask_thread.start()

    while True:

        logger.warning("Starting to do script...")
        do_script()
        logger.warning("✔️ Table updates successfully... ✔️")
        req = get("https://telegrambotkpfuscheduleparser.onrender.com")
        logger.warning("✔️ Request has done... ✔️")

        sleep(SLEEP_TIME)
