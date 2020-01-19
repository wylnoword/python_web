# 蓝图声明,蓝图名+当前路径。一般一个模块才适合做blueprint，单个文件或者视图不适合
# 蓝图需要再注册到app核心对象上才能被访问
# 一个蓝图管理多个视图文件，将蓝图的声明放在模块的__init__文件中
from flask import Blueprint

bp = Blueprint('con', __name__)


# 引入蓝图管理的视图文件
from app.web import controller
from app.web import controller1
