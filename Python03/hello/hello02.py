# -*- coding:utf-8 -*-

from flask import Flask

app = Flask(__name__)

#root로 연결될때
@app.route('/')
def hello_root():
    return '<h1>Hello</h1><a href="/flask">flask</a>'

#flask로 연결될때
@app.route('/flask')
def hello_flask():
    return '<h1>Flask</h1><a href="/">root</a>'


if __name__ == "__main__":
    app.run()