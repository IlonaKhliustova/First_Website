from flask import Flask
from flask import url_for
app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Вот так создаются сайты!"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')


@app.route('/image_sample')
def image():
    return f'''<img src="{url_for('static', filename='cat.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась">'''
