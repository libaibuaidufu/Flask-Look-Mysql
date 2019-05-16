#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 0016 14:42
# @File    : flask_demo.py
# @author  : dfkai
# @Software: PyCharm

from flask import Flask
from flask_look_models import FlaskLookModels

app = Flask(__name__)
app.config["URL_LIST"] = ["mysql://root:123456@127.0.0.1:3306/metest"]
FlaskLookModels(app)

if __name__ == '__main__':
    app.run()
