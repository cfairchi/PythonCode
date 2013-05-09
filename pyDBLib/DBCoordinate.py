import abc
from DBObject import DBObject

class DBCoordinate(DBObject):
    driveid = ""
    order = ""
    latitude = ""
    longitude = ""

    def getColumns(self):
        cols = []
        cols.append("driveid")
        cols.append("order")
        cols.append("latitude")
        cols.append("longitude")
        return cols

    def toString(self):
        print (self.driveid + "," + self.order + "," + self.latitude + "," + self.longitude)

    def getTableName(self):
        return "coordinates"
