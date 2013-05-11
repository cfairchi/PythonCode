#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sqlite3 as lite
import sys
import DBObject
import urllib2
from DBDrive import DBDrive
from DBCoordinate import DBCoordinate

import xml.etree.ElementTree as ET

mls = "{http://www.opengis.net/gml}MultiLineString"
lsm = "{http://www.opengis.net/gml}lineStringMember"
ls = "{http://www.opengis.net/gml}LineString"
cs = "{http://www.opengis.net/gml}coordinates"
 
def clean(theTxt):
    try:
        theTxt = theTxt.encode('ascii','ignore')
        theTxt = theTxt.replace("\n","")
        theTxt = theTxt.replace(";",",")
        theTxt = theTxt.strip()
        return theTxt
    except Exception, err:
        sys.stderr.write('ERROR in clean(): %s\n' % str(err))
        
def parseCoordinates(theDriveId, theStartIndex, theCoords):
	coords = []
	index = theStartIndex
	splitCoords = theCoords.split(" ")
	for i in range(0,len(splitCoords)-1):
		splitStr = splitCoords[i].split(",")
		point = DBCoordinate()
		point.driveid = theDriveId
		point.routeOrder = index 
		point.longitude = splitStr[0]
		point.latitude = splitStr[1]
		point.insertIntoSQLiteDB("BywayExplorer.db")
		index = index + 1
		coords.append(point)
	
	return coords
	

def findLineString(theDriveId, route, theStartIndex):
	routeCoords = []
	if (route.find(ls) is not None):
    		if (route.find(ls).find(cs) is not None):
			routeCoords = parseCoordinates(theDriveId, theStartIndex, route.find(ls).find(cs).text)
	return routeCoords
	
	
	
	
drive = DBDrive()
drive.createSQLiteTable("BywayExplorer.db",True)
#coord = DBCoordinate()
#coord.createSQLiteTable("BywayExplorer.db",True)
tree = ET.parse("byways.xml")
elem = tree.getroot()
byways = elem.findall("Byway")
breakIndex = 0
for byway in byways:
    drive = DBDrive()
    if (byway.find("id") is not None and byway.find("id").text is not None):
    	drive.driveid = byway.find("id").text
    if (byway.find("Name") is not None and byway.find("Name").text is not None):
    	drive.driveName = byway.find("Name").text
    drive.country = "US"
    if (byway.find("States") is not None):
    	if (byway.find("State") is not None and byway.find("State").text is not None):
    		drive.region = byway.find("States").find("State").text
    drive.startLat = ""
    drive.startLon = ""
    drive.stopLat = ""
    drive.stopLon = ""
    sd = ""
    fd = ""
    if (byway.find("ShortDescription") is not None and byway.find("ShortDescription").text is not None):
    	sd = byway.find("ShortDescription").text
    	
    if (byway.find("FullDescription") is not None and byway.find("FullDescription").text is not None):
    	fd = byway.find("FullDescription").text
    
    drive.shortDescription = clean(sd)
    drive.longDescription = clean(fd)
    #drive.description = clean(sd + fd)
    if (byway.find("Length") is not None and byway.find("Length").text is not None):
    	drive.mileage = byway.find("Length").text
    if (byway.find("SuggestedTime") is not None and byway.find("SuggestedTime").text is not None):
    	drive.timeToAllow = byway.find("SuggestedTime").text
    drive.favorite = "false"
    if (byway.find("Photo") is not None and byway.find("Photo").find("Asset") is not None):
    	asset = byway.find("Photo").find("Asset")
    	if (asset.find("URL") is not None and asset.find("URL").text is not None):
		url = asset.find("URL").text
		iName = "image_extra_" + drive.driveid + ".jpg"
    		drive.image = url
    		if (drive.image != ""):
    			print("Saving " + url + " into " + iName)
    			with open("./images/" + iName,"wb") as f:
                       		f.write(urllib2.urlopen(url).read())
                        
    	if (asset.find("Credits") is not None and asset.find("Credits").text is not None):
    		drive.imageCredits = asset.find("Credits").text
    drive.mapimage = ""
    drive.restrictions = ""
    drive.seasons = ""
    drive.considerations = ""
    drive.directions = ""
    #rootCoords = []    
    #if (byway.find("Route") is not None):
   # 	route = byway.find("Route")
	#if (route.find(mls) is not None):
#		startIndex = 0
#		for lineStringMember in route.find(mls).findall(lsm):
			#tRootCoords = findLineString(drive.driveid, lineStringMember, len(rootCoords))
			#rootCoords = rootCoords + tRootCoords
	#elif (route.find(ls) is not None):
	#	routeCoords = findLineString(drive.driveid, route, 0)

#	breakIndex = breakIndex + 1
#	if (breakIndex > 5):
#		break	 	 
    drive.insertIntoSQLiteDB("BywayExplorer.db")
    print drive.driveid
