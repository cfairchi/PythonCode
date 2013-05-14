#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
import os
import MySQLdb
import sys
import DBObject
import urllib2
import simplekml

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
    
    coords = []
    

    if (not os.path.exists(outFile)):
      print ("SELECT * FROM bywayexplorer_coordinate WHERE driveid='" + driveid + "' ORDER BY routeOrder")
      cur.execute("SELECT * FROM bywayexplorer_coordinate WHERE driveid='" + driveid + "' ORDER BY routeOrder")
      coords = cur.fetchall()
    
      for coord in coords:
        lat = coord["latitude"]
        lon = coord["longitude"]
        ll = (lon,lat,0)
        coords.append(ll)
    
      kml = simplekml.Kml()
      ls = kml.newlinestring(name=driveRow["driveName"])
      ls.coords = coords
      ls.extrude = 0
      ls.altitudemode = simplekml.AltitudeMode.clampToGround
      kml.save(outFile)
          
      print( "Generating KML "  )
      print( "Done Generating: " + outFile + " Total Requests:" + str(totalRequests))
    else:
      print( "File Already Exists: " + outFile)
    driveIndex = driveIndex + 1
    if (driveIndex > 0):
      break
  
except MySQLdb.Error, e:
  print "Error %d: %s" % (e.args[0],e.args[1])
  sys.exit(1)
