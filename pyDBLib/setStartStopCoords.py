#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
import os
import MySQLdb

from DBDrive import DBDrive
from DBCoordinate import DBCoordinate
from chrispwd import getUserName
from chrispwd import getPassword

def getMySqlConnection(theDBName):
  return MySQLdb.Connection(user=getUserName(), passwd=getPassword(), db=theDBName, host='localhost')

con = getMySqlConnection("djangosite")

try:
  totalRequests = 0
  cur = con.cursor(MySQLdb.cursors.DictCursor)
  coord = DBCoordinate()
  cur.execute("SELECT driveid FROM bywayexplorer_drive")
  driveRows = cur.fetchall()
  cur.close()
 
  for drive in driveRows:
    driveid = drive["driveid"]
    cur = getMySqlConnection("djangosite")
    cur = con.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM bywayexplorer_coordinate WHERE driveid = '" + driveid + "' ORDER BY routeOrder")
    coordinates = cur.fetchall()
    cur.close()

    if (len(coordinates) > 0):
      drv = DBDrive()
      drv.driveid = coordinates[0]["driveid"]
      drv.startLat = coordinates[0]["latitude"]
      drv.startLon = coordinates[0]["longitude"]
      last = len(coordinates) - 1 
      drv.stopLat = coordinates[last]["latitude"]
      drv.stopLon = coordinates[last]["longitude"]
      
      # cur = con.cursor()
      # print("UPDATE bywayexplorer_drive SET startLat=" + str(drv.startLat) + ", startLon=" + str(drv.startLon) + ", stopLat=" + str(drv.stopLat) + ", stopLon=" + str(drv.stopLon) + " WHERE driveid='" + str(drv.driveid) + "';")
      # cur.execute("UPDATE bywayexplorer_drive SET startLat=" + str(drv.startLat) + ", startLon=" + str(drv.startLon) + ", stopLat=" + str(drv.stopLat) + ", stopLon=" + str(drv.stopLon) + " WHERE driveid='" + str(drv.driveid) + "'"  )
      # con.commit
      # cur.close()

      cur = con.cursor()
        
      cur.execute("UPDATE bywayexplorer_drive SET startLat = %s WHERE driveid = %s", (str(drv.startLat), drv.driveid))        
      print drv.driveid + " Number of rows updated: %d" % cur.rowcount
      cur.execute("UPDATE bywayexplorer_drive SET startLon = %s WHERE driveid = %s", (str(drv.startLon), drv.driveid))        
      print drv.driveid + " Number of rows updated: %d" % cur.rowcount
      cur.execute("UPDATE bywayexplorer_drive SET stopLat = %s WHERE driveid = %s", (str(drv.stopLat), drv.driveid))        
      print drv.driveid + " Number of rows updated: %d" % cur.rowcount
      cur.execute("UPDATE bywayexplorer_drive SET stopLon = %s WHERE driveid = %s", (str(drv.stopLon), drv.driveid))        
      print drv.driveid + " Number of rows updated: %d" % cur.rowcount
      cur.close()

except MySQLdb.Error, e:
  print "Error %d: %s" % (e.args[0],e.args[1])
  sys.exit(1)
