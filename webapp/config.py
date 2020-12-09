import os
import json

# For production (Unix)
with open('/etc/webserveri/zavrsni/config.json') as config_file:
    config = json.load(config_file)


class Config:
    """
        Settings for Flask, user password reset via Email and PSQL
    """

    # For development (Win)
    # SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")
    # PSQL_HOST = os.environ.get("PSQL_HOST")
    # PSQL_PORT = os.environ.get("PSQL_PORT")
    # PSQL_USER = os.environ.get("PSQL_USER")
    # PSQL_PASSWORD = os.environ.get("PSQL_PASS")
    # PSQL_DATABASE = os.environ.get("PSQL_DATABASE")
    # MAIL_SERVER = "smtp.googlemail.com"
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get("EMAIL_USER")
    # MAIL_PASSWORD = os.environ.get("EMAIL_PASS")

    # For production (Unix)
    SECRET_KEY = config.get("FLASK_SECRET_KEY")
    PSQL_HOST = config.get("PSQL_HOST")
    PSQL_PORT = config.get("PSQL_PORT")
    PSQL_USER = config.get("PSQL_USER")
    PSQL_PASSWORD = config.get("PSQL_PASS")
    PSQL_DATABASE = config.get("PSQL_DATABASE")
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = config.get("EMAIL_USER")
    MAIL_PASSWORD = config.get("EMAIL_PASS")

    # MQTT
    MQTT_BROKER_URL = '172.105.76.166'
    MQTT_BROKER_PORT = 1883
