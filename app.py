import random
from flask import Flask, jsonify
import httper
from app import create_app


# app核心模块的初始化，使用__init__文件进行初始化函数声明
app = create_app()


if __name__ == '__main__':
    app = Flask(__name__)
    app.config.from_object('config')
