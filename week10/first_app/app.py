from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return '<h1>Welcome to my page!</h1>'


@app.route('/sayhi')
def hello():
    return '<h1>Hello, World!</h1>'
    