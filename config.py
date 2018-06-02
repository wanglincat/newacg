#encoding utf-8
import os
DEBUG=True

SECRET_KEY=os.urandom(24)

HOSTNAME = ''
PORT     = ''
DATABASE = ''
USERNAME = ''
PASSWORD = ''
DB_URI   ='mysql+mqldb://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,
                                                            HOSTNAME,PORT,DATABASE )
SQLALCHEMY_DATABASE_URI=DB_URI