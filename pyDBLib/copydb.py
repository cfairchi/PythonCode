#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
import os
import sqlite3
from DBDrive import DBDrive
from DBCoordinate import DBCoordinate

con = sqlite3.connect("BywayExplorer.db")
try:
  totalRequests = 0
  cur = con.cursor()
  drive = DBDrive()
  cur.execute("SELECT * FROM " + drive.getTableName())
  driveRows = cur.fetchall()
  print(len(driveRows))
  for driveRow in driveRows:
    driveid = driveRow[0]
    newDrive = DBDrive()
    newDrive.driveid = driveRow[0]
    newDrive.driveName = driveRow[1].replace("'","''")
    newDrive.country = driveRow[2]
    newDrive.region = driveRow[3]
    newDrive.startLat = driveRow[4]
    newDrive.startLon = driveRow[5]
    newDrive.stopLat = driveRow[6]
    newDrive.stopLon = driveRow[7]
    newDrive.shortDescription = ""
    newDrive.longDescription = driveRow[8].replace("'","''")
    newDrive.mileage = driveRow[9]
    newDrive.timeToAllow = driveRow[10]
    newDrive.favorite = driveRow[11]
    newDrive.image = driveRow[12]
    newDrive.mapimage = driveRow[13]
    newDrive.restrictions = driveRow[14]
    newDrive.seasons = driveRow[15]
    newDrive.considerations = driveRow[16]
    newDrive.directions = driveRow[17]
    newDrive.imageCredits = driveRow[18]
    newDrive.insertIntoMySQLDB("djangosite","bywayexplorer_drive")
except sqlite3.Error, e:
  print "Error %d: %s" % (e.args[0],e.args[1])
  sys.exit(1)
finally:
  if con:
    con.close() 

    
  


