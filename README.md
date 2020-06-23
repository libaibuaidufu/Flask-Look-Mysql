#### 一个 通过 flask 查看 mysql 表结构 的插件

##### 目前只支持mysql

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
FlaskLookMysql(app, blueprint_api="db", url_prefix="/db", index="db") # 注意配置 避免冲突

if __name__ == '__main__':
    app.run()

# http://127.0.0.1:5000/db/metest
```
##### 更新
###### 2020-06-23
更新支持werkzeug 最新版，因最新版删除 werkzeug.contrib.cache，因此安装cachelib使用

 ![image](https://github.com/libaibuaidufu/Flask-Look-Mysql/blob/master/doc_img.png) 
