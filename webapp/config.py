import os


class Config:
    # Generate app secret key with secrets.token_hex(16)
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")

    # PostgreSQL server connection parameters
    PSQL_SERVER_HOST = os.environ.get("HOME_AUTO_PSQL_HOST")
    PSQL_SERVER_PORT = os.environ.get("HOME_AUTO_PSQL_PORT")
    PSQL_SERVER_DATABASE = os.environ.get("HOME_AUTO_PSQL_DATABASE")
    PSQL_SERVER_PASSWORD = os.environ.get("HOME_AUTO_PSQL_PASS")

    # Setup for mail account (used for password resetting)
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("EMAIL_USER")
    MAIL_PASSWORD = os.environ.get("EMAIL_PASS")