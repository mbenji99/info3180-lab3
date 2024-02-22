import os
from dotenv import load_dotenv

env_path = ".env"
if os.path.isfile(env_path):
    load_dotenv(dotenv_path=env_path)


class Config(object):
    """Base Config Object"""
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'localhost') 
    MAIL_PORT = os.environ.get('MAIL_PORT', '25') 
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') 
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    
class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False