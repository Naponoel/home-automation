from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from webapp.config import Config
from flask_mqtt import Mqtt


bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'main.landing_page'
login_manager.login_message_category = 'info'
mqtt = Mqtt()


def create_app():
    app = Flask(__name__)
    with app.app_context():
        app.config.from_object(Config)
        bcrypt.init_app(app)
        mqtt.init_app(app)
        login_manager.init_app(app)
        from webapp.routes.all import main
        app.register_blueprint(main)
        from webapp.database.api import api
        app.register_blueprint(api)
    return app


