# 一个 通过 flask 查看 mysql 表结构 的插件

## 安装
```
pip install flask-look-models
```

## 使用
```python
from flask import Flask
from flask_look_models import FlaskLookModels

app = Flask(__name__)
app.config["URL_LIST"] = ["mysql://root:123456@127.0.0.1:3306/metest"]
FlaskLookModels(app)

if __name__ == '__main__':
    app.run()

# http://127.0.0.1:5000/db/metest
```
