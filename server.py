#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from bulb import BulbController

app = Flask(__name__)
bulb_controller = BulbController()


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/kasa/state')
def kasa_state():
    return bulb_controller.state()


if __name__ == '__main__':
    app.run(host="0.0.0.0")
