#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Project : FlaskDemo
# @File : __init__.py.py
# @Time : 2020/3/30 15:49
# @Author : xiao
# @Email : xiaojiaweix@163.com
# @Version : 1.0
# @Descriptions : 创建Flask对象并用app初始化其他组件，如SQLAlchemy，Migrate，views路由等

# here put the import lib
from App.config import env
from App.views import init_views
from ext import init_ext
from flask import Flask
from settings import RUN_MODE


def create_app():
    """
    创建Flask对象，注册其他组件并返回创建的Flask对象
    :return: Flask对象
    """
    app = Flask(__name__)

    # 从配置文件获取配置信息并添加到app，主要包括数据库信息和启动模式
    app.config.from_object(env.get(RUN_MODE))
    # 初始化第三方扩展和组件
    init_ext(app)
    # 注册views视图路由
    init_views(app)
    return app



