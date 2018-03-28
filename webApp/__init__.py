# Configuration Application
__version__ = '0.1'
from flask import Flask
import os

app = Flask('webApp')
app.config['SECRET_KEY'] = os.urandom(24)
app.debug = True
from webApp.controllers import *
