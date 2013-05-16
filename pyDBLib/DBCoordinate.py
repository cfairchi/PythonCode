import abc
from DBObject import DBObject

class DBCoordinate(DBObject):
    driveid = ""
    subRoute = ""
    routeOrder = ""
    latitude = "unknown"
    longitude = ""

    def getColumns(self):
        cols = []
        cols.append(["driveid","TEXT"])
        cols.append(["subRoute","INT"])
        cols.append(["routeOrder","INT"])
        cols.append(["latitude","TEXT"])
        cols.append(["longitude","TEXT"])
        return cols

    def toString(self):
        print (self.driveid + "," + str(self.subRoute) + "," + str(self.routeOrder) + "," + self.latitude + "," + self.longitude)
    
    def getValues(self):
        values = {}
        values["driveid"] = self.driveid
        values["subRoute"] = self.subRoute
        values["routeOrder"] = self.routeOrder
        values["latitude"] = self.latitude
        values["longitude"] = self.longitude
        return values
        
    def getTableName(self):
        return "coordinates"
        
    
