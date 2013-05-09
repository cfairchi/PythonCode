import abc
from DBObject import DBObject

class DBCoordinate(DBObject):
    driveid = ""
    order = ""
    latitude = "unknown"
    longitude = ""

    def getColumns(self):
        cols = []
        cols.append(["driveid","TEXT"])
        cols.append(["order","INT"])
        cols.append(["latitude","TEXT"])
        cols.append(["longitude","TEXT"])
        return cols

    def toString(self):
        print (self.driveid + "," + str(self.order) + "," + self.latitude + "," + self.longitude)
    
    def getValues(self):
        values = {}
        values["driveid"] = self.driveid
        values["order"] = self.order
        values["latitude"] = self.latitude
        values["longitude"] = self.longitude
        return values
        
    def getTableName(self):
        return "coordinates"
