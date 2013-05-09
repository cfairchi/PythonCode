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
		cols.append(["id","TEXT"])
		cols.append(["driveName","TEXT"])
		cols.append(["country","TEXT"])
		cols.append(["region","TEXT"])
		cols.append(["startLat","TEXT"])
		cols.append(["startLon","TEXT"])
		cols.append(["stopLat","TEXT"])
		cols.append(["stopLon","TEXT"])
		cols.append(["description","TEXT"])
		cols.append(["mileage","TEXT"])
		cols.append(["timeToAllow","TEXT"])
		cols.append(["favorite","TEXT"])
		cols.append(["image","TEXT"])
		cols.append(["mapimage","TEXT"])
		cols.append(["restrictions","TEXT"])
		cols.append(["seasons","TEXT"])
		cols.append(["considerations","TEXT"])
		cols.append(["directions","TEXT"])
		cols.append(["imageCredits","TEXT"])
		cols.append(["coordinates","TEXT"])
		return cols

	def toString(self):
		print (self.driveid + "," + self.driveName + "," + self.country + "," + self.region + "," + self.startLat + "," + self.startLon + "," + self.stopLat + "," + self.stopLon + "," + self.description + "," + self.mileage + "," + self.timeToAllow + "," + self.favorite + "," + self.image + "," + self.mapimage + "," + self.restrictions + "," + self.seasons + "," + self.considerations + "," + self.directions + "," + self.imageCredits + "," + self.coordinates)
		
	def getTableName(self):
		return "drives"
