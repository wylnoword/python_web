from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    # 调用蓝图注册方法
    register_blue_print(app)
    return app


# 将蓝图注册到app核心模块上
def register_blue_print(app):
    # 导入蓝图的声明
    from app.web import bp
    # app核心模块注册该蓝图
    app.register_blueprint(bp)
