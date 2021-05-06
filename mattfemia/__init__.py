from flask import Flask, Blueprint
from flask_mail import Mail
import os

mail = Mail()

def create_app():
    """ Init app with application context """

    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')

    # Init dependencies with app context format
    mail.init_app(app)

    with app.app_context():
        from .main import main

        app.register_blueprint(blueprint=main.main,
                                url_prefix='',
                                subdomain='',
                                url_defaults='')

        return app