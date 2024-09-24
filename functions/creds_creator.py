""" Создание JSON-файла Credentials.json ("creds.json"), необходимого для подключения
    сервисного аккаунта и связи с Google Sheets """
from json import dumps
from os import getenv


# Создание JSON-файла [Credentials.json]:
def creds_create():

    # Создание словаря с данными ключа от сервисного аккаунта Google.
    # Некоторые значения словаря заменены на переменные среды:
    credentials = {
        "type": "service_account",
        "project_id": getenv("GOOGLE_PROJECT_ID"),
        "private_key_id": getenv("GOOGLE_PROJECT_KEY_ID"),
        "private_key": getenv("GOOGLE_PRIVATE_KEY").replace('\\n', '\n'),
        "client_email": getenv("GOOGLE_CLIENT_EMAIL"),
        "client_id": getenv("GOOGLE_CLIENT_ID"),
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/" + getenv("GOOGLE_CLIENT_CERT"),
        "universe_domain": "googleapis.com"
    }

    # Преобразование словаря в JSON-файл:
    json_obj = dumps(credentials, indent=4)

    # Сохранение JSON-файла:
    with open("functions/creds.json", "w") as outfile:
        outfile.write(json_obj)
