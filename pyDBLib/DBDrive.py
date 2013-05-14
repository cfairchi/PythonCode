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
		driveid = theRow["driveid"]
		driveName = theRow["driveName"]
		country = theRow["country"]
		region = theRow["region"]
		startLat = theRow["startLat"]
		startLon = theRow["startLon"]
		stopLat = theRow["stopLat"]
		stopLon = theRow["stopLon"]
		shortDescription = theRow["shortDescription"]
		longDescription = theRow["longDescription"]
		mileage = theRow["mileage"]
		timeToAllow = theRow["timeToAllow"]
		favorite = theRow["favorite"]
		image = theRow["image"]
		mapimage = theRow["mapimage"]
		restrictions = theRow["restrictions"]
		seasons = theRow["seasons"]
		considerations = theRow["considerations"]
		directions = theRow["directions"]
		imageCredits = theRow["imageCredits"]
	
	def toString(self):
		print (self.driveid + "," + self.driveName + "," + self.country + "," + self.region + "," + self.startLat + "," + self.startLon + "," + self.stopLat + "," + self.stopLon + "," + self.shortDescription  + "," + self.longDescription + "," + self.mileage + "," + self.timeToAllow + "," + self.favorite + "," + self.image + "," + self.mapimage + "," + self.restrictions + "," + self.seasons + "," + self.considerations + "," + self.directions + "," + self.imageCredits)
		
	def getTableName(self):
		return "drives"
