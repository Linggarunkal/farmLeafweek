# -*- coding: utf-8 -*-

from webApp import app
from flask import render_template, jsonify
from webApp.library.connection import *
from webApp.library.config import *
from webApp.models.auth import signup, passwdHash, signin
from webApp.models.catalog import cataloglist
import json

# GET Process
@app.route('/')
def start():
    return render_template('printer/index.html')


@app.route('/testing2')
def testing2():
    from webApp.models.Printer import status
    jab = status()
    state = 'manager'
    print jab.get_jabatan(state)
    return jsonify({'Message': 'list manager', 'value': jab.get_jabatan(state)})


# isi catalog foto, nama, harga return value, id catalog(for link)
@app.route('/catalog/investment')
def cataloginvest():
    catalog = cataloglist()
    listcatalog = catalog.listreview()
    print listcatalog
    return listcatalog


@app.route('/catalog/investment/<catalogid>')
def catalogdetailinvert(catalogid):
    catalog = cataloglist()
    detCat = catalog.detailCatalog(catalogid)
    return detCat


@app.route('/username/<user>')
def username(user):
    return jsonify({'Message': 'Username', 'name': user})


# Post Status
@app.route('/postRegistration')
def postregistration():
    fname = 'akbar'
    lname = 'Wijayanto'
    email = 'akbar@mail.com'
    passwd = 'akbar'

    hashpasswd = passwdHash()
    passwdencrypt = hashpasswd.passwdEncrypt(passwd)
    usersignup = signup(fname, lname, email, passwdencrypt)
    postusersignup = usersignup.registration()
    return jsonify({'code': 200, 'message': postusersignup, 'Message02': passwdencrypt})


@app.route('/postUserLogin')
def postuserlogin():
    email = 'akbar@mail.com'
    password = 'akbar'

    loginuser = signin(email, password)
    postlogin = loginuser.login()
    return postlogin
