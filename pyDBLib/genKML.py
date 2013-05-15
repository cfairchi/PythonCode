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

def createLineStringKML(theDBDrive, theCoords, theOutFile):
  print( "Generating KML for " + theDBDrive.driveid)
  f = open(theOutFile,"w+")
  f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>" + os.linesep)
  f.write("<kml xmlns=\"http://earth.google.com/kml/2.0\">" + os.linesep)
  f.write("<Document>" + os.linesep)
  f.write("<name>" +  theDBDrive.driveName + "</name>" + os.linesep)
  f.write("<description>" + theDBDrive.shortDescription + "</description>" + os.linesep)
  f.write("<LineString><coordinates>" + os.linesep)
  for coord in theCoords:
    lat = coord["latitude"]
    lon = coord["longitude"]
    ll = (lon,lat,0)
    f.write(str(lat) + "," + str(lon) + ",0 ")
  f.write("</coordinates></LineString>" + os.linesep)    
  f.write("</Document> </kml>")
  f.close()
  
  
try:
  totalRequests = 0
  cur = con.cursor(MySQLdb.cursors.DictCursor)
  cur.execute("SELECT * FROM bywayexplorer_drive")
  driveRows = cur.fetchall()
  
  driveIndex = 0
  for driveRow in driveRows:
    driveid = driveRow["driveid"]
    drive = DBDrive()
    drive.setValues(driveRow)
    #drive.driveId = driveRow["driveid"]
    #drive.shortDescription = driveRow["shortDescription"]
    #drive.driveName = driveRow["driveName"]
    outFile = "kml_" + driveid + ".kml"
    if (not os.path.exists(outFile)):
      print ("SELECT * FROM bywayexplorer_coordinate WHERE driveid='" + driveid + "' ORDER BY routeOrder")
      cur.execute("SELECT * FROM bywayexplorer_coordinate WHERE driveid='" + driveid + "' ORDER BY routeOrder")
      coords = cur.fetchall()
      createLineStringKML(drive,coords,outFile)  
    else:
      print( "File Already Exists: " + outFile)
    driveIndex = driveIndex + 1
    if (driveIndex > 0):
      break
  
except MySQLdb.Error, e:
  print "Error %d: %s" % (e.args[0],e.args[1])
  sys.exit(1)
