from flask import Flask, request
from flask_login import LoginManager
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_moment import Moment
from flask_babel import Babel

db = SQLAlchemy()
mail = Mail()
moment = Moment()
babel = Babel()
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "auth.login"


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(create_app().config['LANGUAGES'])


def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    babel.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    return app
