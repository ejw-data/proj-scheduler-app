from flask import Flask
from db_paths import path


def create_app():
    '''
    Initiate Flask
    '''
    app = Flask(__name__)


    ENV = 'dev'

    if ENV == 'dev':
        app.debug = True
        app.config['SQLALCHEMY_DATABASE_URI'] = path["scheduler"]
        app.config['SQLALCHEMY_BINDS'] = {
            'scheduler':    path["scheduler"]
        }
    elif ENV == 'prod':
        app.debug = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'webaddress'
        app.config['SQLALCHEMY_BINDS'] = {
            'login':    'sqlite:///login-flask.db',
            'utility':  'sqlite:///utility.db'
        }
    else:
        print("Please select an environment:  developement or production.")

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app
