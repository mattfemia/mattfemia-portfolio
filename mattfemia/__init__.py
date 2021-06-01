from flask import Flask, Blueprint
from flask_mail import Mail
import os

mail = Mail()

def create_app():
    """ Init app with application context """

    app = Flask(__name__)
    app.config.from_object('config.ProductionConfig')

    # Init dependencies with app context format
    mail.init_app(app)

    with app.app_context():
        from .main import main
        from .clonotypr import clonotypr

        app.register_blueprint(blueprint=main.main,
                                url_prefix='',
                                subdomain='',
                                url_defaults='')
        
        app.register_blueprint(blueprint=clonotypr.clonotypr,
                                url_prefix='/clonotypr',
                                subdomain='',
                                url_defaults='')

        return app