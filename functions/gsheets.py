""" Копирование таблицы формата XLSX в таблицу Google Sheets """
import gspread
import openpyxl


# Функция для переноса Excel-таблицы в Google Sheets.
# Строка t_path - путь к таблице.
def gs_transfer(t_path: str) -> None:

    # Открытие таблицы:
    wb = openpyxl.open(t_path)
    ws = wb.active

    # Матрица с данными таблицы:
    matrix = []

    # Сохраняем значение каждой ячейки таблицы в матрицу:
    for i in range(1, ws.max_row + 1):
        row = []
        for j in range(1, ws.max_column + 1):
            row.append(ws.cell(row=i, column=j).value)
        matrix.append(row)

    # Предоставляем боту доступ к Google Sheets:
    gc = gspread.service_account(filename='functions/creds.json')

    # Открываем таблицу Google Sheets:
    worksheet = gc.open("KPFU_Schedule_Online").sheet1

    # Чистим устаревшую информацию в Google Sheets, затем - обновляем её:
    worksheet.clear()
    worksheet.update(matrix, 'A1')
