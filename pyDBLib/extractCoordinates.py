#!/usr/bin/python
# _*_ coding: utf-8 _*_

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
coord = DBCoordinate()

tree = ET.parse("byways.xml")
elem = tree.getroot()
byways = elem.findall("Byway")
breakIndex = 0
for byway in byways:
    drive = DBDrive()
    if (byway.find("id") is not None and byway.find("id").text is not None):
    	drive.driveid = byway.find("id").text
    
    rootCoords = []    
    if (byway.find("Route") is not None):
     	route = byway.find("Route")
	    if (route.find(mls) is not None):
        subRoute = 0
  		  startIndex = 0
  		  for lineStringMember in route.find(mls).findall(lsm):
			    tRootCoords = findLineString(drive.driveid, lineStringMember, len(rootCoords))
			    rootCoords = rootCoords + tRootCoords
	      elif (route.find(ls) is not None):
	        routeCoords = findLineString(drive.driveid, route, 0)

#	breakIndex = breakIndex + 1
#	if (breakIndex > 5):
#		break	 	 
    drive.insertIntoSQLiteDB("BywayExplorer.db")
    print drive.driveid
