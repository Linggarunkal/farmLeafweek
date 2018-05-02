from webApp.library.connection import *
from webApp.library.config import *
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

        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            condDetail = 'catalog_id = %s'
            detailLivestock = conn.select('cataloginvestment', condDetail, 'catalog_id,nameCatalog,slotPrice,contractperiod,returnInvest,sharingPeriod,slotAvaible,catalogPicture', catalog_id=self.catalogid)
            getDetailLivestock = []
            for index, list in enumerate(detailLivestock):
                strSlotPrice = decimal.Decimal(list[2])
                strSlotAvaible = decimal.Decimal(list[6])

                i = {
                    "catalogId": list[0],
                    "nameCatalog": list[1],
                    "slotPrice": str(strSlotPrice),
                    "contractPeriod": list[3],
                    "returnInvest": list[4],
                    "sharingPeriod":  list[5],
                    "slotAvaible": str(strSlotAvaible),
                    "catalogPicture": list[7]
                }

                getDetailLivestock.append(i)
            return getDetailLivestock
        except Exception as e:
            return "Error Database: %s" % str(e)

    def catalogReview(self, catalogid):
        self.catalogid = catalogid
        try:
            conn = mysqlconnection(HOST,USERNAME,PASSWORD,DATABASE)
            condCatalogid = 'catalog_id = %s'
            getCatReview = conn.select('review_detail', condCatalogid, '*', catalog_id=self.catalogid)

            detailReview = []
            for index, list in enumerate(getCatReview):
                strRate = decimal.Decimal(list[5])

                i = {
                    "custname": list[3],
                    "custPicture": list[4],
                    "rate": str(strRate),
                    "comment": list[6],
                    "reviewdate": list[7]
                }
                detailReview.append(i)
            return detailReview
        except Exception as e:
            return "Error Database: %s" % str(e)

    def catROIInvest(self, catalogid):
        self.catalogid = catalogid

        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            condInvest = 'catalog_id = %s'
            getInvest = conn.select('v_catalogroi_invest', condInvest, '*', catalog_id=self.catalogid)

            detInvestVal = []
            for index, list in enumerate(getInvest):
                i = {
                    "catalogroi_id": list[0],
                    "catalog_id": list[1],
                    "mount1": list[2],
                    "mount2": list[3],
                    "mount3": list[4],
                    "mount4": list[5],
                    "mount5": list[6],
                    "mount6": list[7],
                    "mount7": list[8],
                    "mount8": list[9],
                    "mount9": list[10],
                    "mount10": list[11],
                    "mount11": list[12],
                    "mount12": list[13]
                }
                detInvestVal.append(i)
            return detInvestVal
        except Exception as e:
            return "Error Database: %s" % str(e)

    def catROIReturn(self, catalogid):
        self.catalogid = catalogid
        try:
            conn = mysqlconnection(HOST, USERNAME, PASSWORD, DATABASE)
            condInvest = 'catalog_id = %s'
            getInvest = conn.select('v_catalogroi_return', condInvest, '*', catalog_id=self.catalogid)

            detReturnVal = []
            for index, list in enumerate(getInvest):
                i = {
                    "catalogroi_id": list[0],
                    "catalog_id": list[1],
                    "mount1": list[2],
                    "mount2": list[3],
                    "mount3": list[4],
                    "mount4": list[5],
                    "mount5": list[6],
                    "mount6": list[7],
                    "mount7": list[8],
                    "mount8": list[9],
                    "mount9": list[10],
                    "mount10": list[11],
                    "mount11": list[12],
                    "mount12": list[13]
                }
                detReturnVal.append(i)
            return detReturnVal
        except Exception as e:
            return "Error Database: %s" % str(e)
