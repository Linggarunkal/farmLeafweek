from webApp.library.connection import *
from webApp.library.config import *
from flask import jsonify


class cataloglist(object):
    def listreview(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            listCatalog = conn.select('cataloginvestment', None, 'catalog_id, nameCatalog, contractPeriod, returnInvest, sharingPeriod, catalogPicture, slotAvaible, slotPrice')
            print listCatalog
            return jsonify({'code': 200, 'Message': len(listCatalog)})
        except Exception as e:
            return "Error Database: %s" % str(e)