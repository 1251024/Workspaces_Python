# -*- coding:utf-8 -*-

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "hello, world"

if __name__ == '__main__':
    app.run()

# 127.0.0.1:5000 복사해서 web에 접속하기