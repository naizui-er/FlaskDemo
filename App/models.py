#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Project : FlaskDemo
# @File : models.py
# @Time : 2020/3/30 15:47
# @Author : xiao
# @Email : xiaojiaweix@163.com
# @Version : 1.0
# @Descriptions : web实体类及其各种数据库操作

# here put the import lib
from ext import db


class User(db.Model):
    """User model"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))

    # 添加user
    def add(self):
        # 使用由SQLAlchemy提供的session进行数据库操作，session即会话
        db.session.add(self)
        db.session.commit()



"""在这里添加业务中的各种实体类（参考User类的形式）"""















