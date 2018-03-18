# -*- coding: utf-8 -*-
from flask import flash
from webApp.library.connection import *
from webApp.library.config import *


class Printer(object):

    def show_string(self, text):
        if text == '':
            flash("You didn't enter any text to flash")
        else:
            flash(text + "!!!")


class status(object):
    def get_jabatan(self, value):
        conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
        whereValue = 'nama_jabatan = %s'
        jabatan = conn.select('jabatan', whereValue, 'id_jabatan, nama_jabatan', jabatan='manager')
        return jabatan


# process handling to database or other data source and bussiness logic