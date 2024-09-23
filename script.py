""" Скрипт, реализующий парсинг таблицы с расписанием и перенос обновлённой таблицы в Google Sheets """
from functions.creds_creator import creds_create
from functions.separator import separate_merges
from functions.gsheets import gs_transfer
from functions.parser import parsing
from dotenv import load_dotenv
from urllib import request
from constant import link
from time import sleep
import logging


logger = logging.getLogger(__name__)
load_dotenv()
creds_create()


def do_script() -> None:

    # Загрузка таблицы:
    request.urlretrieve(link, "tables/RawTable.xlsx")

    # Программа реализуется за счёт последовательной работы трёх функций:
    separate_merges("tables/RawTable.xlsx", "tables/PreparedTable.xlsx")
    parsing("tables/PreparedTable.xlsx", "tables/CookedTable.xlsx")
    gs_transfer("tables/CookedTable.xlsx")


while True:
    try:
        logger.warning("Starting to do script")
        do_script()
        logger.warning("Table updates successfully...")
    except Exception as e:
        logger.warning(f"ERROR: {e}")

    sleep(600)
