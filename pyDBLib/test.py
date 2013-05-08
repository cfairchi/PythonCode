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
    drive.driveid = byway.find("id").text
    drive.driveName = byway.find("Name").text
    drive.country = "US"
    drive.region = byway.find("States").find("State").text
    drive.startLat = ""
    drive.startLon = ""
    drive.stopLat = ""
    drive.stopLon = ""
    drive.description = byway.find("ShortDescription").text + byway.find("FullDescription").text
    drive.mileage = byway.find("Length").text
    drive.timeToAllow = byway.find("SuggestedTime").text
    drive.favorite = "false"
    drive.image = byway.find("Photo").find("URL").text
    drive.imageCredits = byway.find("Photo").find("Credits").text
    drive.mapimage = ""
    drive.restrictions = ""
    drive.seasons = ""
    drive.considerations = ""
    drive.directions = ""
    drive.coordinates = byway.find("Route")

