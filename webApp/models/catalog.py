from webApp.library.connection import *
from webApp.library.config import *
from flask import jsonify, json


class cataloglist(object):
    def listreview(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            listCatalog = conn.select('cataloginvestment', None, 'nameCatalog, contractPeriod, returnInvest, sharingPeriod, slotPrice, slotAvailable')
            return jsonify({'code': 200, 'Message': listCatalog})
        except Exception as e:
            return "Error Database: %s" % str(e)


