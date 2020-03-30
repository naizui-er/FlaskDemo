#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Project : FlaskDemo
# @File : __init__.py.py
# @Time : 2020/3/30 16:17
# @Author : xiao
# @Email : xiaojiaweix@163.com
# @Version : 1.0
# @Descriptions : web视图路由注册及初始化，以供其他文件调用，在views文件夹下添加视图后需要在这里注册一下才能生效

# here put the import lib
from .views import blue
from .views2 import blue2


def init_views(app):
    """
    初始化views
    :param app: Flask对象
    :return:
    """
    # 注册路由视图
    app.register_blueprint(blue)
    app.register_blueprint(blue2)

    """在这里注册新添加的蓝图（参考views.pyhe views2.py的形式）"""