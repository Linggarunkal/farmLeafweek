from webApp.library.connection import *
from webApp.library.config import *
from webApp.library.response_message import messages
from webApp.library.connection import mysqlconnection
from webApp.library.config import HOST, USERNAME, PASSWORD, DATABASE
import decimal

class livestockFarm(object):
    def showHomeLivestock(self):
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            getHomeLivestock = conn.select('cataloginvestment', None, 'catalog_id,nameCatalog,returnInvest,catalogPicture,slotPrice')

            getAllLivestock = []
            for index, list in enumerate(getHomeLivestock):
                strReturnInvest = decimal.Decimal(list[2])
                strSlotPrice = decimal.Decimal(list[4])

                i = {
                    "catalogId": list[0],
                    "namaCatalog": list[1],
                    "returnInvest": str(strReturnInvest),
                    "catalogPicture": list[3],
                    "slotPrice": str(strSlotPrice)
                }
                getAllLivestock.append(i)
            return getAllLivestock
        except Exception as e:
            return "Error Database: %s" % str(e)

    def showDetailLivestock(self, catalogid):
        self.catalogid = catalogid
        # nama investasi
        # harga slot
        # contract period
        # return investment
        # profit sharing period
        # available slot
        # description
        # review
        # roi simulation
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            condDetail = 'catalog_id = %s'
            detailLivestock = conn.select('cataloginvestment', condDetail, '', catalog_id=self.catalogid)
            getDetailLivestock = []
            for index, list in enumerate(detailLivestock):
                str
            return "tempe"
        except Exception as e:
            return "Error Database: %s" % str(e)