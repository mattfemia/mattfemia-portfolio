import os

class Config:
    ''' Global configs for main site and /projects '''

    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Mail Config
    MAIL_USERNAME = os.environ.get('SMTP_USERNAME')
    MAIL_PASSWORD = os.environ.get('SMTP_PASSWORD')
    MAIL_SERVER = os.environ.get('SMTP_SERVER')
    MAIL_PORT = os.environ.get('SMTP_PORT')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_SUPPRESS_SEND = False

class ProductionConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    MAIL_DEBUG = True