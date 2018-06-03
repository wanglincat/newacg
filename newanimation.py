#encoding: utf-8

from flask import Flask,render_template
import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/animation/<name>')
def animation(name):

    return '<h1>helllo,%s</h1>'% name

@app.route('/animationcommit')
def animationcommit():
    pass
if __name__ == '__main__':
    app.run()
