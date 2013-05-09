import abc
from DBObject import DBObject

class DBCoordinate(DBObject):
    driveid = ""
    order = ""
    latitude = "unknown"
    longitude = ""

    def getColumns(self):
        cols = []
        cols.append("driveid")
        cols.append("order")
        cols.append("latitude")
        cols.append("longitude")
        return cols

    def toString(self):
        print (self.driveid + "," + str(self.order) + "," + self.latitude + "," + self.longitude)

    def getTableName(self):
        return "coordinates"
