#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sqlite3 as lite
import sys
import DBObject
from DBDrive import DBDrive
import xml.etree.ElementTree as ET
		

drive = DBDrive()
drive.createSQLiteTable("BywayExplorer.db",True)
tree = ET.parse("byways.xml")
elem = tree.getroot()
byways = elem.findall("Byway")
for byway in byways:
    drive = DBDrive()
    if (byway.find("id") isnot None):
    	drive.driveid = byway.find("id").text
    if (byway.find("Name") isnot None):
    	drive.driveName = byway.find("Name").text
    drive.country = "US"
    if (byway.find("States") isnot None):
    	if (byway.find("State") isnot None):
    		drive.region = byway.find("States").find("State").text
    drive.startLat = ""
    drive.startLon = ""
    drive.stopLat = ""
    drive.stopLon = ""
    drive.description = byway.find("ShortDescription").text + byway.find("FullDescription").text
    if (byway.find("Length") isnot None):
    	drive.mileage = byway.find("Length").text
    if (byway.find("SuggestedTime") isnot None):
    	drive.timeToAllow = byway.find("SuggestedTime").text
    drive.favorite = "false"
    if (byway.find("Photo") is not None):
    	if (byway.find("Photo").find("URL") is not None):
    		drive.image = byway.find("Photo").find("URL").text
    	if (byway.find("Photo").find("Credits") is not None):
    		drive.imageCredits = byway.find("Photo").find("Credits").text
    drive.mapimage = ""
    drive.restrictions = ""
    drive.seasons = ""
    drive.considerations = ""
    drive.directions = ""
    if (byway.find("Route") isnot None):
    	drive.coordinates = byway.find("Route")
    drive.toString()
