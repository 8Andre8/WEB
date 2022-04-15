from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='Привет, Мир! (ЛР2)', text='Hello, World! (ЛР2)')


if __name__ == '__main__':
    app.run()