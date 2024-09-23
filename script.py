""" Скрипт, реализующий парсинг таблицы с расписанием и перенос обновлённой таблицы в Google Sheets """
from functions.creds_creator import creds_create
from functions.separator import separate_merges
from functions.gsheets import gs_transfer
from functions.parser import parsing
from dotenv import load_dotenv
from urllib import request
from constant import link
from requests import get
from flask import Flask
from time import sleep
import threading
import logging
import os


logger = logging.getLogger(__name__)
app = Flask(__name__)
load_dotenv()
creds_create()


# Функция, запускающая приложение Flask:
def run_application():
    app.run(host="0.0.0.0", port=os.getenv("PORT"))


@app.route('/')
def hello_world():
    return 'Wake Up! You must work!'


# Функция, выполняющая скрипт - парсинг:
def do_script() -> None:
    # Загрузка таблицы:
    request.urlretrieve(link, "tables/RawTable.xlsx")

    # Программа реализуется за счёт последовательной работы трёх функций:
    separate_merges("tables/RawTable.xlsx", "tables/PreparedTable.xlsx")
    parsing("tables/PreparedTable.xlsx", "tables/CookedTable.xlsx")
    gs_transfer("tables/CookedTable.xlsx")


if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_application)
    flask_thread.start()

    while True:
        try:
            logger.warning("Starting to do script...")
            do_script()
            logger.warning("✔️ Table updates successfully... ✔️")
            req = get("https://telegrambotkpfuscheduleparser.onrender.com")
            logger.warning("✔️ Request has done... ✔️")
        except Exception as e:
            logger.warning(f"❌ ERROR: {e} ❌")

        sleep(600)
