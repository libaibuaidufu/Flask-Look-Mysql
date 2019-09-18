#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 0016 11:04
# @File    : setup.py
# @author  : dfkai
# @Software: PyCharm


from setuptools import setup, find_packages

setup(
    name='Flask_Look_Mysql',
    version='1.0.4',
    keywords='flask look mysql html',
    description='a look mysql html',
    license='MIT License',
    url='https://github.com/libaibuaidufu/Flask-Look-Mysql',
    author='libaibuaidufu',
    author_email='libaibuaidufu@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    install_requires=["flask", "pymysql"],
)
