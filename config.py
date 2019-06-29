import os

BASE_PATH = os.path.abspath(os.path.dirname(__file__))


class Config():
    SECRET_KEY = os.environ.get("SECRET_KEY") or "testing"
    SQLALCHEMY_DATABASE_URI = (os.environ.get("DB_URL") or
                               "sqlite:///{}".format(os.path.join(BASE_PATH,
                                                                  "app.db")))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
