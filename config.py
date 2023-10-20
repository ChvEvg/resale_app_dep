import logging
import os


basedir = os.path.abspath(os.path.dirname(__file__))

DB_NAME = 'resale.db'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, DB_NAME)
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False

CSRF_ENABLED = True
SECRET_KEY = 'sdgsdfgsdfgdfg'


LOGGING = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] [%(levelname)s] - %(name)s: %(message)s',
        },
    },

    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'filename': 'resale.log',
        },
    },

    'loggers': {
        'resale': {
            'handlers': ['file', ],
            'level': logging.DEBUG
        },
    },
}