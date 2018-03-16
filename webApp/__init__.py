# -*- coding: utf-8 -*-
__version__ = '0.1'
from flask import Flask

app = Flask('webApp')
app.config['SECRET_KEY'] = 'random'
app.debug = True
from webApp.controllers import *
