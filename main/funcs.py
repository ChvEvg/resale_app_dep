import logging

from flask import render_template, request

logger = logging.getLogger('resale')


def homepage():
    try:
        logger.debug('homepage started')
        context = {
            'title': 'Домашняя страница',
        }
        return render_template('index.html', context=context)
    except Exception as ex:
        logger.warning(ex)
    finally:
        logger.debug('homepage finished')