from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 创建Flask应用实例
app = Flask(__name__)
# 配置数据库连接字符串
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Tigerqiuqiu!925424@127.0.0.1:5432/zc'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 创建SQLAlchemy实例
db = SQLAlchemy(app)


def my_decorator(func):
    def wrapper():
        print("Something is before my_decorator")
        func()
        print("Something is after my_decorator")
        return wrapper


@my_decorator
def say_hello():
    print("Hello!")
    return ""


# 定义/hello路由及其处理函数
@app.route('/hello', methods=['GET'])
def hello():
    result = ""
    try:
        result: str = say_hello()
    except TypeError:
        print('Object is not callable')
    return f"Hello, World! {result}"


@app.route('/employee', methods=['GET'])
def employee():
    return "Hello, World!"


# 测试数据库连接
@app.route('/testdb')
def testdb():
    try:
        # 执行简单的查询以测试连接
        result = db.engine.execute("SELECT 1")
        return "Database Connected!" if result else "Connection failed!"
    except Exception as e:
        return f"An error occurred: {e}"


# 启动Flask应用
if __name__ == '__main__':
    app.run(debug=True)
