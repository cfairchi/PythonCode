#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
import os
import MySQLdb
import sys
import DBObject
import urllib2
import pykml
from pykml.factory import KML_ElementMaker as KML

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
    outFile = "kml_" + driveid + ".kml"
    #kmlFile = pykml.kml(outFile)
    ls = KML.LineString()
    coords = KML.coordinates()
    ls.AltitudeMode = mode.clampToGround

    if (not os.path.exists(outFile)):
      print ("SELECT * FROM bywayexplorer_coordinate WHERE driveid='" + driveid + "' ORDER BY routeOrder")
      cur.execute("SELECT * FROM bywayexplorer_coordinate WHERE driveid='" + driveid + "' ORDER BY routeOrder")
      coords = cur.fetchall()
    
      for coord in coords:
        lat = coord["latitude"]
        lon = coord["longitude"]
        ls.Coordinates.append(lat,lon,0)
        coordList.append(str(lat) + "," + str(lon) + ",0")
        totalRequests = totalRequests + 1
      
      pm = pykml.Placemark()
      pm.setGeometry(ls)
      pm.description = drive["shortDescription"]
      pm.addTofolder(driveid)
      kmlFile.placemarks.append(pm)
          
      print( "Generating KML "  )
      kmlFile.write()
      print( "Done Generating: " + outFile + " Total Requests:" + str(totalRequests))
    else:
      print( "File Already Exists: " + outFile)
    driveIndex = driveIndex + 1
    if (driveIndex > 0):
      break
  
except MySQLdb.Error, e:
  print "Error %d: %s" % (e.args[0],e.args[1])
  sys.exit(1)
