#encoding utf-8
import os
DEBUG=True

SECRET_KEY=os.urandom(24)

HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'acg'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI   ='mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,
                                                            HOSTNAME,PORT,DATABASE )
SQLALCHEMY_DATABASE_URI=DB_URI