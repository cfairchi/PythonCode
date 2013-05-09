import abc
from DBObject import DBObject

class DBDrive(DBObject):
  driveid = ""
driveName = ""
country = ""
region = ""
startLat = ""
startLon = ""
stopLat = ""
stopLon = ""
description = ""
mileage = ""
timeToAllow = ""
favorite = ""
image = ""
mapimage = ""
restrictions = ""
seasons = ""
considerations = ""
directions = ""
imageCredits = ""
     coordinates = ""
    

def getColumns(self):
cols = []
cols.append("id")
cols.append("driveName")
cols.append("country")
cols.append("region")
cols.append("startLat")
cols.append("startLon")
cols.append("stopLat")
cols.append("stopLon")
cols.append("description")
cols.append("mileage")
cols.append("timeToAllow")
cols.append("favorite")
cols.append("image")
cols.append("mapimage")
cols.append("restrictions")
cols.append("seasons")
cols.append("considerations")
cols.append("directions")
cols.append("imageCredits")
cols.append("coordinates")
return cols

def toString(self):
print (self.driveid + "," + self.driveName + "," + self.country + "," + self.region + "," + self.startLat + "," + self.startLon + "," + self.stopLat + "," + self.stopLon + "," + self.description + "," + self.mileage + "," + self.timeToAllow + "," + self.favorite + "," + self.image + "," + self.mapimage + "," + self.restrictions + "," + self.seasons + "," + self.considerations + "," + self.directions + "," + self.imageCredits + "," + self.coordinates)

def getTableName(self):
return "drives"
