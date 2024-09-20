""" Скрипт, реализующий парсинг таблицы с расписанием и перенос обновлённой таблицы в Google Sheets """
from functions.separator import separate_merges
from functions.gsheets import gs_transfer
from functions.parser import parsing
from urllib import request
from constant import link
from time import sleep


def do_script() -> None:

    # Загрузка таблицы:
    request.urlretrieve(link, "tables/RawTable.xlsx")

    # Программа реализуется за счёт последовательной работы трёх функций:
    separate_merges("tables/RawTable.xlsx", "tables/PreparedTable.xlsx")
    parsing("tables/PreparedTable.xlsx", "tables/CookedTable.xlsx")
    gs_transfer("tables/CookedTable.xlsx")


while True:
    do_script()
    print('Table updated successfully...')
    sleep(30)
