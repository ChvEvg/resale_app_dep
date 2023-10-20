from resale import app
from flask import render_template
from main.funcs import homepage


# Block of views for common errors custom html
@app.errorhandler(404)
def pageNotFound(error):
    context = {
        'title': 'Страница не найдена'
    }
    return render_template('page404.html', context=context), 404
@app.errorhandler(500)
def serverError(error):
    context = {
        'title': 'Ошибка сервера'
    }
    return render_template('page500.html', context=context), 500

# Block of views for base pages of the web-app

@app.route('/', methods=['GET'])
def index():
    return homepage()
