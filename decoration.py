#encoding: utf-8
from functools import wraps
from flask import session,url_for,redirect
#限制登录装饰器
def login_requried(func):

    @wraps(func)
    def wrapper(*args,**kwargs):
        if session.get('username'):
            return func(*args,**kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper
