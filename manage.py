# author:Sole_idol
# filename: manage.py
# datetime:2020/8/19 7:59
"""
cookie练习
abort()抛出状态码
@app.errorhandler(403)   捕获403状态码，返回数据
"""

from flask import Flask, render_template, request, redirect, abort
from flask_sqlalchemy import SQLAlchemy
from flask import make_response

app = Flask(__name__)
# 数据库连接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://demon:123456@localhost:3306/school'
# 每次请求结束后都会自动提交数据库中的数据
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 创建一个db实例
db = SQLAlchemy(app)


# 重定向
@app.route('/')
def index():
    return redirect('/login/', code=301)


# 抛出403状态码
@app.route('/yichang/')
def abort_1():
    abort(403)
    return '你访问的页面异常...'


# 捕获403状态码，返回数据
@app.errorhandler(403)
def foo1(e):
    return f'服务器拒绝你的请求<br>{e}'


@app.route('/login/', methods=('POST', 'GET'))
def login():
    if request.method == 'POST':
        # 设置cookie
        response = make_response(redirect('/main/'))
        response.set_cookie('user', 'jack')
        return response
    else:
        return render_template('login.html')


@app.route('/main/', methods=('POST', 'GET'))
def main():
    # 获取cookie
    user = request.cookies.get('user')
    # print(user)
    return render_template('main.html', user=user)


if __name__ == '__main__':
    app.run(debug=True)
