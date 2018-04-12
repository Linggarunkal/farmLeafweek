# -*- coding: utf-8 -*-

from webApp import app
from flask import render_template, jsonify, request
from webApp.library.connection import *
from webApp.library.config import *
from webApp.models.auth import signup, passwdHash, signin
from webApp.models.catalog import cataloglist
import os
from webApp.library.response_message import messages


# GET Process
@app.route('/')
def start():
    # images = os.listdir(os.path.join(app.static_folder, "assets/img/slider"))
    # print images
    return render_template('home/home.html')


@app.route("/test/response")
def testResp():
    message = messages(500)
    tempe = message.resp(None)
    return tempe


@app.route('/template/test')
def payment():
    return render_template('base/testing.html')


@app.route('/transaction/review')
def transReview():
    return render_template('transaction/01-review.html')


@app.route('/transaction/payment')
def transPayment():
    return render_template('transaction/02-payment-method.html')


@app.route('/transaction/recieve')
def transRecieve():
    return render_template('transaction/03-payment-recieve.html')


@app.route('/transaction/preparelivestock')
def transPreparelivestock():
    return render_template('transaction/04-prepare-livestock.html')


@app.route('/transaction/breedinglivestock')
def transBreedinglivestock():
    return render_template('transaction/05-payment-breeding-livestock.html')


@app.route('/catalog/investment')
def catInvestment():
    return render_template('catalog/catalog.html')


@app.route('/catalog/investment/detail')
def catInvestDet():
    return render_template('catalog/detail-catalog.html')


@app.route('/demo/simulation')
def demoSimulation():
    return render_template('demo/simulasi.html')



@app.route('/testing2')
def testing2():
    from webApp.models.Printer import status
    jab = status()
    state = 'manager'
    print jab.get_jabatan(state)
    return jsonify({'Message': 'list manager', 'value': jab.get_jabatan(state)})


# isi catalog foto, nama, harga return value, id catalog(for link)
# @app.route('/catalog/investment')
# def cataloginvest():
#     catalog = cataloglist()
#     listcatalog = catalog.listreview()
#     print listcatalog
#     return listcatalog


# @app.route('/catalog/investment/<catalogid>')
# def catalogdetailinvert(catalogid):
#     catalog = cataloglist()
#     detCat = catalog.detailCatalog(catalogid)
#     return detCat


@app.route('/username/<user>')
def username(user):
    return jsonify({'Message': 'Username', 'name': user})


#dasboard user
@app.route('/user/dasboard/home')
def userDasboardHome():
    active = 'home'
    return render_template('user_dasboard/home.html', active=active)


@app.route('/user/dasboard/transaction')
def userDasboardTrans():
    active = 'transaction'
    return render_template('user_dasboard/trans_dasboard.html', active=active)


@app.route('/user/dasboard/disbursement')
def userDasboardDisbursement():
    active = 'disbursement'
    return render_template('user_dasboard/disbursement.html', active=active)


@app.route('/user/dasboard/timeline')
def userDasboardTimeline():
    active = 'timeline'
    return render_template('user_dasboard/timeline.html', active=active)


@app.route('/user/dasboard/weight')
def userDasboardweight():
    active = 'berat'
    return render_template('user_dasboard/home.html', active=active)


@app.route('/user/dasboard/feedback')
def userDasboardFeedback():
    active = 'feedback'
    return render_template('user_dasboard/home.html', active=active)

@app.route('/user/dasboard/invoice')
def userDasboardInvoice():
    return render_template('user_dasboard/invoice.html')


@app.route('/user/dasboard/profile')
def userDasboardProfile():
    return render_template('user_dasboard/profile.html')


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
