#encoding: utf-8

from flask import Flask,render_template,request,redirect,url_for
import config
from models import User
from exts import db

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    else:
        pass

@app.route('/regist/',methods=['GET','POST'])
def regist():
    if request.method=='GET':
        return render_template('regist.html')
    else:
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        #判断用户名是否已经注册
        user=User.query.filter(User.username==username).first()
        if user:
            return u'该用户名已经被注册了，请更换'
        else:
            if password1!=password2:
                return u'两次密码不一样，请核对'
            else:
                user=User(username=username,password=password1)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))








@app.route('/animation/<name>')
def animation(name):

    return '<h1>helllo,%s</h1>'% name

@app.route('/animationcommit')
def animationcommit():
    pass
if __name__ == '__main__':
    app.run()
