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
blue2 = Blueprint("blue2", __name__)


@blue2.route("/index")
def index():
    return 'Hello index!'


# 其实使用了migrate数据库迁移扩展后这个路由就可以删除了
@blue2.route("/createdb2")
def create_db2():
    db.create_all()
    return "create DB sccuessful"


@blue2.route("/dropdb2")
def drop_db2():
    db.drop_all()
    return "delete DB sccuessful"


@blue2.route("/adduser2")
def add_user2():
    user = User()
    user.username = "testuser"
    # 添加user（使用这种方法需要在user的model中添加对应的方法）
    #user.add()
    # 或者
    db.session.add(user)
    db.session.commit()
    return "create user sccuessful"


"""在这里添加业务中的路由（各种Service操作）"""





