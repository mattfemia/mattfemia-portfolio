from flask import Flask, Blueprint
import os

def create_app():
    """ Init app with application context """

    app = Flask(__name__)
    app.config.from_object('config.ProductionConfig')

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