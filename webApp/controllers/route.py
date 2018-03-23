# -*- coding: utf-8 -*-

from webApp import app
from flask import render_template, jsonify
from webApp.library.connection import *
from webApp.library.config import *
from webApp.models.auth import getUser


@app.route('/')
def start():
    return render_template('printer/index.html')


@app.route('/testing')
def testing():
    conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
    jabatan = conn.select('jabatan', None, 'id_jabatan, nama_jabatan')
    return jsonify({'Message': 'Testing', 'value': jabatan})


@app.route('/testing2')
def testing2():
    from webApp.models.Printer import status
    jab = status()
    state = 'manager'
    print jab.get_jabatan(state)
    return jsonify({'Message': 'list manager', 'value': jab.get_jabatan(state)})


@app.route('/tahu')
def tahu():
    return render_template('tahu.html')


@app.route('/print')
def printer():
    return render_template('printer/print.html')


@app.route('/profile')
def profile():
    return jsonify({'Message': 'ini from page yang profile'})


@app.route('/tempe')
def tempe():
    return jsonify({'Message': 'ini tempe page'})


@app.route('/catalog/invertment')
def catalogInvert():
    return jsonify({'Message': 'list all catalog investnment'})


@app.route('/catalog/invertment/<catalogid>')
def catalogDetailInvert(catalogid):
    return jsonify({'Message': 'Jagung baakar', 'code': catalogid})


@app.route('/username/<user>')
def username(user):
    return jsonify({'Message': 'Username', 'name': user})


@app.route('/hi')
def hi():
    user = getUser()
    telo = user.show()
    length = len(telo[0])
    return jsonify({'code': 200, 'message': telo[0], 'length': length})