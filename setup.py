#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Name    : setup.py
# @Author  : yanlee

import setuptools
import shutil

# 删除dist/目录
shutil.rmtree('dist', ignore_errors=True)

setuptools.setup(
    name="awesome-systematic-trading",
    version="1.31.5",
    author="yanjlee",
    author_email="yanjlee@163.com",
    description="Awesome Systematic Trading：We are collecting a list of resources papers, softwares, books, articles for finding, developing, and running systematic trading (quantitative trading) strategies.",  # 模块简介
    install_requires=[
        'requests',
        'faker',
        'execjs',
        'loguru',
        'base64',
        'hashlib',
        'Crypto',
        'pandas',
        'fuzzywuzzy',
        'httpx',
        'Pillow',
        'playwright',
        'PyExecJS',
        'redis',
        'fastapi',
        'uvicorn',
        'APScheduler',
        'beautifulsoup4',
        'bs4',
        'certifi',
        'clickhouse-driver',
        'curl-cffi',
        'DrissionPage',
        'fake-useragent',
        'Flask',
        'Flask-APScheduler',
        'Flask-Cors',
        'frida',
        'gevent',
        'httpx',
        'Jinja2',
        'langchain',
        'langchain-community',
        'suiutils-py',
    ],
    long_description=open(r'readme.md', encoding='utf-8').read(),  # 读取readme自述文件
    long_description_content_type="text/markdown",
    url="https://github.com/yanjlee/awesome-systematic-trading",  # 模块github地址
    packages=setuptools.find_packages(),     # 自动列出项目下的包
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",   # 开源许可证
        "Operating System :: OS Independent",      # 这里的定义是系统无关（全平台兼容），如果你的包只能在部分特定系统上运行，需要修改。
    ],
)