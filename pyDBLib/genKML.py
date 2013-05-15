#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
import os
import MySQLdb
import sys
import DBObject


from DBDrive import DBDrive
from DBCoordinate import DBCoordinate
from DBDrive import DBDrive
from chrispwd import getUserName
from chrispwd import getPassword

def getMySqlConnection(theDBName):
  return MySQLdb.Connection(user=getUserName(), passwd=getPassword(), db=theDBName, host='localhost')

con = getMySqlConnection("djangosite")
#con.autocommit(True);

def createLineStringKML(theDriveId, theCoords, theOutFile):
  print( "Generating KML for " + theDriveId)
  
  for coord in theCoords:
    lat = coord["latitude"]
    lon = coord["longitude"]
    ll = (lon,lat,0)
    

try:
  totalRequests = 0
  cur = con.cursor(MySQLdb.cursors.DictCursor)
  cur.execute("SELECT * FROM bywayexplorer_drive")
  driveRows = cur.fetchall()
  
  driveIndex = 0
  for driveRow in driveRows:
    driveid = driveRow["driveid"]
    outFile = "kml_" + driveid + ".kml"
    if (not os.path.exists(outFile)):
      print ("SELECT * FROM bywayexplorer_coordinate WHERE driveid='" + driveid + "' ORDER BY routeOrder")
      cur.execute("SELECT * FROM bywayexplorer_coordinate WHERE driveid='" + driveid + "' ORDER BY routeOrder")
      coords = cur.fetchall()
      createLineStringKML(driveid,coords,outFile)  
    else:
      print( "File Already Exists: " + outFile)
    driveIndex = driveIndex + 1
    if (driveIndex > 0):
      break
  
except MySQLdb.Error, e:
  print "Error %d: %s" % (e.args[0],e.args[1])
  sys.exit(1)
