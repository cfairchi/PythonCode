#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
import os
import MySQLdb
import sys
import DBObject
import urllib2
from csf_StreetView import generateVideoFromCoords
from DBDrive import DBDrive
from DBCoordinate import DBCoordinate
from DBDrive import DBDrive
from chrispwd import getUserName
from chrispwd import getPassword

def getMySqlConnection(theDBName):
  return MySQLdb.Connection(user=getUserName(), passwd=getPassword(), db=theDBName, host='localhost')

con = getMySqlConnection("djangosite")
#con.autocommit(True);

try:
  totalRequests = 0
  cur = con.cursor(MySQLdb.cursors.DictCursor)
  cur.execute("SELECT * FROM bywayexplorer_drive")
  driveRows = cur.fetchall()
  
  driveIndex = 0
  for driveRow in driveRows:
    driveid = driveRow["driveid"]
    outFile = "video_" + driveid
    if (not os.path.exists(outFile)):
      coordList = []
      print ("SELECT * FROM bywayexplorer_coordinate WHERE driveid='" + driveid + "' ORDER BY routeOrder")
      cur.execute("SELECT * FROM bywayexplorer_coordinate WHERE driveid='" + driveid + "' ORDER BY routeOrder")
      coords = cur.fetchall()
    
      for coord in coords:
        lat = coord["latitude"]
        lon = coord["longitude"]
        coordList.append(lat + "," + lon + "," + 0)
        totalRequests = totalRequests + 1
      
      print( "Generating: " + outFile)
      generateVideoFromCoords(coordList,driveid + "_video")
      print( "Done Generating: " + outFile + " Total Requests:" + totalRequests)
    else:
      print( "File Already Exists: " + outFile)
    driveIndex = driveIndex + 1
    
