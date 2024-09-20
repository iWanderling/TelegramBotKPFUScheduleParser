""" Загрузка таблицы с расписанием, разделение объединённых ячеек. Подготовка таблицы к парсингу """
from constant import *
import openpyxl


# Функция-разделитель объединённых в таблице ячеек.
# Строка t_path - путь к таблице;
# Строка dest - путь, по которому нужно сохранить обновлённую таблицу.
def separate_merges(t_path: str, dest: str) -> None:

    # Открытие и чтение таблицы
    wb = openpyxl.open(t_path)
    ws = wb.active

    # Список диапазонов объединённых ячеек
    merged_cells = list(map(str, ws.merged_cells.ranges))

    # Разделяем каждый объединённый диапазон
    for merge in merged_cells:
        ws.unmerge_cells(range_string=merge)

    # Форматируем данные о диапазонах для работы с ними
    merged_cells = [d.split(":") for d in merged_cells]

    # Разделение объединённых ячеек:
    for merge_cell in merged_cells:

        # Диапазон объединённых ячеек
        d = merge_cell

        # Значение, которое должно быть в каждой ячейке, относящейся к диапазону
        top_left_value = ws[d[0]].value

        # Создаём начальный флаг (вносим данные от крайней левой ячейки до крайней правой)
        start = columns.index(d[0][0])

        # Создаём конечный флаг:
        if 'AA' not in d[1]:
            finish = columns.index(d[1][0])
        else:
            finish = 26

        # Номер ряда, на котором будут происходить изменения
        row = d[0][1:]

        # Проходимся по каждой ячейке, вносим в неё данные
        for i in range(start, finish + 1):
            ws[f'{columns[i]}{row}'] = top_left_value

    # Сохранение таблицы:
    wb.save(dest)
