import random

from flask import jsonify, request

import httper
from ..valid import controller
from . import bp


# 返回值类容有一定约束
from ..valid.controller import validate


@bp.route('/')
def hello_world0():
    a = 10
    b = 5
    c = 1
    return str((a + b) / c)


# 如何获取前端参数。类比spring的@RequestParam注解
# http://127.0.0.1:5000/args?arg0=str1&arg1=wwww
@bp.route('/args')
def arg():
    # request中有http请求的大量信息，类比servlet中的request对象
    var1 = request.args['arg0']
    var2 = request.args['arg1']
    list0 = [var1, var2]
    # return jsonify(list0)
    return str(list0)


# 如何参数验证。WTforms
# 规则 0<arg0<10,args1的位数<10
# 注意！ flask将异常存在errors中，不主动抛出，需要手动继承校验器，完成全局异常的捕获和封装
@bp.route('/valid')
def valid():
    # var1 = request.args['arg0']
    # var2 = request.args['arg1']
    valid = validate(request.args)
    # 开启校验,返回TRUE为验证通过，否则验证不通过
    if valid.validate():
        ex = valid.errors
        # 从 表单valid中取参数
        var1 = valid.arg0.data
        var2 = valid.arg1.data
        list0 = [var1, var2]
        return str(list0)
    else:
        # 存放错误的errors元组
        print(valid.errors['arg0'])
        return str('验证失败')


# 如何进行路由。类比spring的@PathVariable注解
@bp.route('/uuid/<a>/<b>')
def hello_world1(a, b):
    print('路由的参数为%s, %s', str(a), str(b))
    return 'uuid'


# 如何进行错误异常处理。 try except语句块进行捕捉
@bp.route('/int')
def hello_world2():
    try:
        return str(random.randint(0, 100))
    except TypeError:
        return '输出错误'


# 如何发起一个GET请求。使用requests包的get方法，直接传入URL地址进行请求
@bp.route('/get')
def http():
    r = httper.HTTP.get(url='http://127.0.0.1:8080/time', return_json=False)

    print(r)
    return r


# 如何向前端返回一个JSON串 使用jsonify()进行包裹json串进行返回。可以将响应Content-Type: conlication/json
@bp.route('/json')
def json():
    r = httper.HTTP.get(url='http://127.0.0.1:8080/json', return_json=False)
    print('这是响应： ' + str(r))
    return jsonify(r)
