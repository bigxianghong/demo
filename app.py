# encoding=utf8
from flask import Flask,render_template

app = Flask(__name__)
# session 生成随机数种子，用于
app.config['SECRET_KEY']

#定义接口地址
@app.route('/index')
def hello_world():
    name = "大喜"
    return "接口测试"


#请求参数的问题：
#url地址再带的查询参数：http：//x.x.x./test?username=aaa&bbb=111
#通过flask自定义的路由规则和参数：http：//x.x.x./test/a/<a>
#post请求的参数，通过post征文传输。

#路由地址参数，路由地址参数必须同步定义在接口函数里面作为该参数的形参
#可以显示数据类型
'''
@app.route('/article/<int:articleid>-<page>')
def article(articleid):
    return f"你正在访问编号：{articleid}的文章"
'''


if __name__ == '__main__':
    app.run(host='0.0.0.0',port='50001')
