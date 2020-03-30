#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Project : FlaskDemo
# @File : __init__.py.py
# @Time : 2020/3/30 15:49
# @Author : xiao
# @Email : xiaojiaweix@163.com
# @Version : 1.0
# @Descriptions : 项目入口文件

# here put the import lib
from App import create_app
from flask_migrate import MigrateCommand
from flask_script import Manager

# 创建Flask对象
app = create_app()
# 将Flask对象交给flask-Manager管理
manager = Manager(app=app)
# 添加Migrate数据库迁移命令，db表示使用db xxxx进行操作，如：【数据库初始化命令】：python manage.py db init
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()

    """
    操作数据库命令：
        - 初始化：
            python manage.py db init
        - 生成迁移文件：
            python manage.py db migrate
        - 创建数据库：
            python manage.py db upgrade
    启动命令：
        - 单线程：
            python manage.py runserver -p 8001 -d -r
        - 多线程：
            python manage.py runserver -p 8001 -d -r --threaded
    """
