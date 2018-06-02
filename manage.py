#encoding: utf-8

from flask_script import Manager
from flask_migrate import Migrate,MigrateComman
from newanimation import app
from exts import db

manager = Manager(app)

#使用Migrate绑定app和db
migrate = Migrate(app,db)

#添加迁移脚本命令
manager.add_command('db',MigrateComman)

if __name__=="__main__":
    manager.run()