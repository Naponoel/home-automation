from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from webapp.config import Config
from flask_marshmallow import Marshmallow


bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'main.landing_page'
login_manager.login_message_category = 'info'
marsh = Marshmallow()
# mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    with app.app_context():
        app.config.from_object(Config)

        marsh.init_app(app)
        bcrypt.init_app(app)
        login_manager.init_app(app)
        # mail.init_app(app)

        # Import & Register blueprints
        from webapp.main.routes import main
        app.register_blueprint(main)
        from webapp.controlers.routes import controlers
        app.register_blueprint(controlers)
        from webapp.backend.routes import backend
        app.register_blueprint(backend)

    return app
