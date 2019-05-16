#### 一个 通过 flask 查看 mysql 表结构 的插件

##### 安装
```
pip install flask-look-mysql
```

##### 使用
```python
from flask import Flask
from flask_look_mysql import FlaskLookMysql

app = Flask(__name__)
app.config["URL_LIST"] = ["mysql://root:123456@127.0.0.1:3306/metest"]
FlaskLookMysql(app)

if __name__ == '__main__':
    app.run()

# http://127.0.0.1:5000/db/metest
```
