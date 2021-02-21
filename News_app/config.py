import os
from sys import platform

if platform == "win32":
    basedir = os.path.abspath(os.path.dirname(__file__))
else:
    basedir = os.path.abspath(os.getcwd())

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY') or \
    'abc123ced456'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_TOKEN_EXPIRES = False
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = os.getenv('SECRET_KEY') or 'abc123ced456'