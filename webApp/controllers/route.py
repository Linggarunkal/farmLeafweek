# -*- coding: utf-8 -*-
from webApp import app
from flask import render_template, jsonify


@app.route('/')
def start():
    return render_template('printer/index.html')


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


#handling front end and handling request from user