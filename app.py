# -*- coding: utf-8 -*-
"""
@Author: 王剑威
@Time: 2020/10/23 1:55 下午
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Travis-CI"


if __name__ == '__main__':
    app.run()
