""" Собрание переменных, содержащих информацию, которая используется при парсинге.
    Необходимо для корректной работы программы """

# Ссылки на загрузку таблицы:
LINKS = ["https://kpfu.ru/portal/docs/F_851501052/grafik_konsul_2024_25_uch_god_1_sem_1_kurs.xlsx",
         "https://kpfu.ru/portal/docs/F1134952167/grafik_konsul_2024_25_uch_god_1_sem_2_kurs.xlsx",
         "https://kpfu.ru/portal/docs/F922459678/grafik_konsul_2024_25_uch_god_1_sem_3_kurs.xlsx",
         "https://kpfu.ru/portal/docs/F352282606/grafik_konsul_2024_25_uch_god_1_sem_4_kurs.xlsx"]

REMOVEDLINKTEXT = ["Ссылка на консультацию:", "Ссылка на консультацию", "Ссылки на консультацию:",
                   "Ссылки на консультацию", "ссылка на трансляцию для зрителей:",
                   "Cсылка на трансляцию для зрителей:", "Ссылки на трансляцию для зрителей:",
                   "Ссылка на видеовстречу для организатора и участников:", ';']

# Дни недели:
DAYS = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']

# Буквенные названия колонок таблицы:
COLUMNS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
           'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AM']

# Список списков групп каждого курса (от 1-го до 4-го):
GROUPS = [

          ['09-401', '09-402', '09-403', '09-411(1)', '09-411(2)', '09-412(1)', '09-412(2)', '09-413(1)', '09-413(2)',
           '09-414(1)', '09-414(2)', '09-421', '09-422', '09-431(1)', '09-431(2)', '09-441', '09-442', '09-443',
           '09-451', '09-452', '09-453', '09-454', '09-461', '09-462', '09-463', '09-464'],

          ['09-301', '09-302', '09-303(1)', '09-303(2)', '09-311(1)', '09-311(2)', '09-312(1)', '09-312(2)',
           '09-313(1)', '09-313(2)', '09-314(1)', '09-314(2)', '09-321', '09-322', '09-331(1)', '09-331(2)',
           '09-332(1)', '09-332(2)', '09-341', '09-342', '09-343', '09-351', '09-352', '09-353', '09-361',
           '09-362', '09-363'],

          ['09-201', '09-202', '09-203', '09-211', '09-212', '09-213', '09-221', '09-222', '09-231', '09-241', '09-251',
           '09-252(1)', '09-252(2)', '09-253(1)', '09-253(2)', '09-254(1)', '09-254(2)', '09-261', '09-262', '09-263'],

          ['09-101', '09-102', '09-103', '09-111', '09-112', '09-113', '09-121', '09-122', '09-131', '09-132', '09-141',
           '09-142', '09-151', '09-152', '09-153', '09-161', '09-162', '09-163']

          ]


# Данные ячеек <День Недели>, <Начало>, <Окончание> и цвета к ним:
DATA_COLUMNS = [('День Недели', 'FA8072'), ("Начало", "F0E68C"), ("Окончание", "90EE90")]

# Ширина и длина ячеек:
CWIDTH = 20
CHEIGHT = 80

# Время перерыва работы скрипта (в секундах)
SLEEP_TIME = 600
