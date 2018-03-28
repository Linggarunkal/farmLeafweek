from webApp.library.connection import *
from webApp.library.config import *
from flask import jsonify
import decimal

class cataloglist(object):
    def listreview(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            listCatalog = conn.select('cataloginvestment', None, 'catalog_id, nameCatalog, contractPeriod, returnInvest, sharingPeriod, catalogPicture, slotAvaible, slotPrice')
            catalog = []
            for index, list in enumerate(listCatalog):
                catalog_id = str(list[0])
                namacatalog = str(list[1])
                contractperiod = str(list[2])
                returninvest = str(list[3])
                sharingperiod = str(list[4])
                catalogpicture = str(list[5])
                slotavaible = str(decimal.Decimal(list[6]))
                slotprice = str(decimal.Decimal(list[7]))

                i = {
                    'catalog_id': catalog_id,
                    'namaCatalog': namacatalog,
                    'contactPeriod': contractperiod,
                    'returnInvest': returninvest,
                    'sharingPeriod': sharingperiod,
                    'catalogPicture': catalogpicture,
                    'slotAvaible': slotavaible,
                    'slotPrice': slotprice
                }
                catalog.append(i)
            if len(catalog) > 0:
                return jsonify({'code': 200, 'Message': catalog})
            else:
                return jsonify({'code': 205, 'Message': 'Data Not Found on System'})
        except Exception as e:
            return jsonify({'code': 500, 'Message': "Error Database: %s" % str(e)})

    def detailCatalog(self, detailid):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            condCatalog = 'catalog_id = %s'
            detCatalog = conn.select('cataloginvestment', condCatalog, 'catalog_id, nameCatalog, contractPeriod, returnInvest, sharingPeriod,catalogPicture, slotAvaible, slotPrice', catalog_id=detailid)
            catalogDetail = []

            for index, list, in enumerate(detCatalog):
                catalog_id = str(list[0])
                namacatalog = str(list[1])
                contractperiod = str(list[2])
                returninvest = str(list[3])
                sharingperiod = str(list[4])
                catalogpicture = str(list[5])
                slotavaible = str(decimal.Decimal(list[6]))
                slotprice = str(decimal.Decimal(list[7]))

                i = {
                    'catalog_id': catalog_id,
                    'namaCatalog': namacatalog,
                    'contactPeriod': contractperiod,
                    'returnInvest': returninvest,
                    'sharingPeriod': sharingperiod,
                    'catalogPicture': catalogpicture,
                    'slotAvaible': slotavaible,
                    'slotPrice': slotprice
                }
                catalogDetail.append(i)
            if len(catalogDetail) > 0:
                return jsonify({'code': 200, 'Message': catalogDetail})
            else:
                return jsonify({'code': 205, 'Message': 'Data Not Found on System'})

        except Exception as e:
            return jsonify({'code': 500, 'Message': "Error Database: %s" % str(e)})
