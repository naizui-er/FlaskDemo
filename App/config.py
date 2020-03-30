#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Project : FlaskDemo
# @File : config.py
# @Time : 2020/3/30 18:20
# @Author : xiao
# @Email : xiaojiaweix@163.com
# @Version : 1.0
# @Descriptions : 项目中主要的配置文件

# here put the import lib

import os

# 运行根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_sql_uri(database_info):
    """
    格式化URI
    :param database_info:  数据库连接信息
    :return: 格式化后的URI
    """
    engine = database_info.get("ENGINE") or "sqlite"
    driver = database_info.get("DRIVER") or "sqlite"
    user = database_info.get("USER") or ""
    password = database_info.get("PASSWORD") or ""
    host = database_info.get("HOST") or ""
    port = database_info.get("PORT") or ""
    database_name = database_info.get("DATABASE_NAME") or ""

    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, password, host, port, database_name)


class Config:
    DEBUG = False
    TESTING = False

    # SQLAlchemy在将来版本中可能加入SQLALCHEMY_TRACK_MODIFICATIONS参数，默认为False，为了保持与未来版本的兼容性，
    # 官方建议添加此参数，否则将会给出warning
    # 默认即可不需要改动
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DebugConfig(Config):
    """调试环境配置"""
    DEBUG = True
    DATABASE_INFO = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "root",
        "HOST": "localhost",
        "PORT": "3306",
        "DATABASE_NAME": "FlaskDemoDB"
    }

    SQLALCHEMY_DATABASE_URI = get_sql_uri(DATABASE_INFO)


class DevelopConfig(Config):
    """开发环境配置"""
    DEBUG = True
    DATABASE_INFO = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "root",
        "HOST": "localhost",
        "PORT": "3306",
        "DATABASE_NAME": "FlaskDemoDB"
    }

    SQLALCHEMY_DATABASE_URI = get_sql_uri(DATABASE_INFO)


class TestingConfig(Config):
    """测试环境配置"""
    TESTING = True
    DATABASE_INFO = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "root",
        "HOST": "localhost",
        "PORT": "3306",
        "DATABASE_NAME": "FlaskDemoDB"
    }

    SQLALCHEMY_DATABASE_URI = get_sql_uri(DATABASE_INFO)


class ProductConfig(Config):
    """生产环境配置"""
    DATABASE_INFO = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "root",
        "HOST": "localhost",
        "PORT": "3306",
        "DATABASE_NAME": "FlaskDemoDB"
    }

    SQLALCHEMY_DATABASE_URI = get_sql_uri(DATABASE_INFO)


# 启动选项
env = {
    "debug": DebugConfig,
    "develop": DevelopConfig,
    "testing": TestingConfig,
    "product": ProductConfig,
    "default": DevelopConfig
}













