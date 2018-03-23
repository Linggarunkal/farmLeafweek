from webApp.library.connection import *
from webApp.library.config import *
from passlib.hash import sha256_crypt
from flask import jsonify


class signin(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def passwdVerify(self, secret, passwd):
        return sha256_crypt.verify(secret, passwd)

    def login(self):
        try:
            __email = self.email
            __password = self.password
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            cond_email = 'email = %s'
            checkUser = conn.select('users', cond_email, 'email, password', email=__email)
            if (len(checkUser) > 0):
                verify = self.passwdVerify(__password, checkUser[0][1])
                if verify:
                    return jsonify({'status': 200, 'Message': 'Verify User'})
                else:
                    return jsonify({'status': 400, 'Message': 'Failed Credential'})
            else:
                return jsonify({'status': 400, 'Message': 'User not Exist' })

        except Exception as e:
            return "Error Database: %s" % str(e)


class signup(object):
    def __init__(self, fname, lname, email, password):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.password = password

    def passwdEncrypt(self, passwd):
        return sha256_crypt.encrypt(passwd)

    def registration(self):
        try:
            passHash = self.passwdEncrypt(self.password)
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            conn.cursor()
            conn.callproc()

        except Exception as e:
            return "Error Database: %s" % str(e)


class getUser(object):
    def show(self):
        conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
        userAll = conn.select('users', None, '*')
        return userAll