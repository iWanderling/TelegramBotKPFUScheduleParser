import json


# Создание Credentials.json
def creds_create():
    credentials = {
        "type": "service_account",
        "project_id": GOOGLE_PROJECT_ID,
        "private_key_id": GOOGLE_PROJECT_KEY_ID,
        "private_key": GOOGLE_PRIVATE_KEY,
        "client_email": GOOGLE_CLIENT_EMAIL,
        "client_id": GOOGLE_CLIENT_ID,
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/" + GOOGLE_CLIENT_CERT,
        "universe_domain": "googleapis.com"
    }

    json_obj = json.dumps(credentials, indent=4)

    with open("functions/creds.json", "w") as outfile:
        outfile.write(json_obj)
