from base64 import b64encode
import os

RANDOM_KEY = os.urandom(32)
STRING_RANDOM = b64encode(RANDOM_KEY).decode('utf-8')

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    SECRET_KEY = STRING_RANDOM
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sam:dev7331@localhost/sakelist'

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_DEFAULT_SENDER = os.environ.get("MAIL_USERNAME")
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    LANGUAGES = ['en', 'ja']

    UPLOADS_FOLDER = basedir + "\\app\\static\\uploads"
