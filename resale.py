import logging
from logging.config import dictConfig


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import LOGGING


dictConfig(LOGGING)


app = Flask(__name__)
app.config.from_object('config')
app.logger = logging.getLogger('resale')
app.logger.info('resale_started')

import views
