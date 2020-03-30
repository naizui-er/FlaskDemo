#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Project : FlaskDemo
# @File : ext.py
# @Time : 2020/3/30 17:06
# @Author : xiao
# @Email : xiaojiaweix@163.com
# @Version : 1.0
# @Descriptions : 这里用来加载并初始化所有的第三方插件及扩展

# here put the import lib
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# 创建SQLAlchemy数据库操作对象
db = SQLAlchemy()
# 创建Migrate迁移对象
migrate = Migrate()


def init_ext(app):
    """
    初始化第三方扩展
    :param app: manage.py中初始化的Flask对象
    :return:
    notation：
    使用懒加载的原因：解决导包时出现的循环调用问题
    """
    # 通过SQLAlchemy提供的懒加载方式延迟加载app参数，用来解决循环调用问题
    db.init_app(app)
    # 通过Migrate提供的懒加载方式延迟加载app参数，用来解决循环调用问题
    migrate.init_app(app, db)

    """在这里添加各种第三方组件或扩展"""




