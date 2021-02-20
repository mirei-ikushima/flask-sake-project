import os


class Config:

    SAKENOTE_TOKEN = os.environ.get("SAKENOTE_TOKEN")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SAKENOTE_SAKES_BASE_URL = "https://www.sakenote.com/api/v1/sakes?token={0}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sam:dev7331@localhost/sakelist'

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
