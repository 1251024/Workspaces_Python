# -*- coding:utf-8 -*-

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def root():
    return '''
        <a href='/hello'>hello</a><br/><br/>
        <input type='button' value='hello' onclick='location.href="/hello/name"' />
    '''

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/test/', methods=['post']) #methods s가 빠지지 않게 유의하자!!
def test():
    return render_template('test.html', test=request.form['command'])


if __name__ == '__main__':
    app.run()
    
    # render_template: 템플릿 렌더링 해주는 애, html 렌더링할거야
    # html파일은 templates폴더에
    # css파일들은 static폴더에
    