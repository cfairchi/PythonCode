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
	shortDescription = ""
	longDescription = ""
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
    
	def getValues(self):
    		values = {}
    		values["driveid"] = self.driveid
	   	values["driveName"] = self.driveName
		values["country"] = self.country
		values["region"] = self.region
		values["startLat"] = self.startLat
		values["startLon"] = self.startLon
		values["stopLat"] = self.stopLat
		values["stopLon"] = self.stopLon
		values["shortDescription"] = self.shortDescription
		values["longDescription"] = self.longDescription
		values["mileage"] = self.mileage
		values["timeToAllow"] = self.timeToAllow
		values["favorite"] = self.favorite
		values["image"] = self.image
		values["mapimage"] = self.mapimage
		values["restrictions"] = self.restrictions
		values["seasons"] = self.seasons
		values["considerations"] = self.considerations
		values["directions"] = self.directions
		values["imageCredits"] = self.imageCredits
    		return values
	
	def getColumns(self):
		cols = []
		cols.append(["driveid","TEXT"])
		cols.append(["driveName","TEXT"])
		cols.append(["country","TEXT"])
		cols.append(["region","TEXT"])
		cols.append(["startLat","TEXT"])
		cols.append(["startLon","TEXT"])
		cols.append(["stopLat","TEXT"])
		cols.append(["stopLon","TEXT"])
		cols.append(["shortDescription","TEXT"])
		cols.append(["longDescription","TEXT"])
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
		return cols

	def setValues(self, theRow):
		self.driveid = theRow["driveid"]
		self.driveName = theRow["driveName"]
		self.country = theRow["country"]
		self.region = theRow["region"]
		self.startLat = theRow["startLat"]
		self.startLon = theRow["startLon"]
		self.stopLat = theRow["stopLat"]
		self.stopLon = theRow["stopLon"]
		self.shortDescription = theRow["shortDescription"]
		self.longDescription = theRow["longDescription"]
		self.mileage = theRow["mileage"]
		self.timeToAllow = theRow["timeToAllow"]
		self.favorite = theRow["favorite"]
		self.image = theRow["image"]
		self.mapimage = theRow["mapimage"]
		self.restrictions = theRow["restrictions"]
		self.seasons = theRow["seasons"]
		self.considerations = theRow["considerations"]
		self.directions = theRow["directions"]
		self.imageCredits = theRow["imageCredits"]
	
	def toString(self):
		print (self.driveid + "," + self.driveName + "," + self.country + "," + self.region + "," + self.startLat + "," + self.startLon + "," + self.stopLat + "," + self.stopLon + "," + self.shortDescription  + "," + self.longDescription + "," + self.mileage + "," + self.timeToAllow + "," + self.favorite + "," + self.image + "," + self.mapimage + "," + self.restrictions + "," + self.seasons + "," + self.considerations + "," + self.directions + "," + self.imageCredits)
		
	def getTableName(self):
		return "drives"
