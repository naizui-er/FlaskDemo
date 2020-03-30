#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Project : FlaskDemo
# @File : views.py
# @Time : 2020/3/30 15:47
# @Author : xiao
# @Email : xiaojiaweix@163.com
# @Version : 1.0
# @Descriptions : web视图

# here put the import lib
from App.models import db, User
from flask import Blueprint

# 实例化Blueprint蓝图对象，并给他起个名字叫blue
blue = Blueprint("blue", __name__)


@blue.route("/")
def index():
    """
    启动测试
    :return:
    """
    return 'Hello world!'

# 如果使用的是mysql则需要手动创建数据库，这个路由也就没用了可以直接删除
# 如果使用的是sqlite数据库，可以使用这个路由进行数据库创建
@blue.route("/createdb")
def create_db():
    """
    创建数据库
    :return:
    """
    db.create_all()
    return "create DB sccuessful"

# 这个方法一般删除即可，可根据自己业务需求进行取舍
@blue.route("/dropdb")
def drop_db():
    """
    删除数据库
    :return:
    """
    db.drop_all()
    return "delete DB sccuessful"


@blue.route("/adduser")
def add_user():
    """
    添加user
    :return:
    """
    user = User()
    user.username = "testuser"
    # 添加user（使用这种方法需要在user的model中添加对应的方法）
    #user.add()
    # 或者
    db.session.add(user)
    db.session.commit()
    return "create user sccuessful"


"""在这里添加业务中的路由（各种Service操作）"""





