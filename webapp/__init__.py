from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from webapp.config import Config

bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'main.landing_page'
login_manager.login_message_category = 'info'
# mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    with app.app_context():
        app.config.from_object(Config)

        bcrypt.init_app(app)
        login_manager.init_app(app)
        # mail.init_app(app)

        # Import & Register blueprints
        from webapp.main.routes import main
        app.register_blueprint(main)
        # from WebApp.users.routes import users
        # from WebApp.errors.handlers import errors
        # app.register_blueprint(users)
        # app.register_blueprint(errors)

    return app
