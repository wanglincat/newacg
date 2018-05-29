from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/animation/<name>')
def animation(name):

    return '<h1>helllo,%s</h1>'% name

@app.route('/animationcommit')
def animationcommit():
    pass
if __name__ == '__main__':
    app.run()
