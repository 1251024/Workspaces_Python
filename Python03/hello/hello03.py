# -*- coding:utf-8 -*-

from flask import Flask

app = Flask(__name__)


# 값을 보냈더니
@app.route('/')
def hello_root():
    return '<h1><a href="/test/admin">test</a></h1>'

# 값을 받아서 쓸 수 있음
@app.route('/test/<id>')
def hello_test(id):
    return '<h1>hello, ' + id + "</h1>"

if __name__ == '__main__':
    app.run()