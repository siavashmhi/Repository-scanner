from os import environ


class Config:
    ENV = environ.get("GITVISOR_API_ENV", "production")

    DEBUG = bool(int(environ.get("GITVISOR_API_DEBUG", "0")))

    TESTING = bool(int(environ.get("GITVISOR_API_TESTING", "0")))

    SECRET_KEY = environ.get("GITVISOR_API_SECRET_KEY", "secretkey")

    SQLALCHEMY_DATABASE_URI = environ.get(
        "GITVISOR_API_DATABASE_URL",
        "mysql+pymysql://root:siavash@127.0.0.1:33063/mysql",
    )

    SQLALCHEMY_ECHO = DEBUG

    SQLALCHEMY_RECORD_QUERIES = DEBUG

    SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG

    TIMEZONE = environ.get("GITVISOR_API_TIMEZONE", "Europe/London")
