import abc
from DBObject import DBObject

class DBPoi(DBObject):
    poiGroup = ""
    poiName = ""
    latitude = ""
    longitude = ""
    description = ""
    details = ""

    def getColumns(self):
        cols = []
        cols.append(["poiGroup","INT"])
        cols.append(["poiName","TEXT"])
        cols.append(["latitude","TEXT"])
        cols.append(["longitude","TEXT"])
        cols.append(["description","TEXT"])
        cols.append(["details","TEXT"])
        return cols

    def toString(self):
        print (self.poiName)
    
    def getValues(self):
        values = {}
        values["poiGroup"] = self.poiGroup
        values["poiName"] = self.poiName
        values["latitude"] = self.latitude
        values["longitude"] = self.longitude
        values["description"] = self.description
        values["details"] = self.details
        return values
        
    def getTableName(self):
        return "poi"
        
    
