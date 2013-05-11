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
  if con1:
    con1.close()
    
  for drive in driveRows:
    driveid = drive["driveid"]
    con2 = getMySqlConnection("djangosite")
    cur2 = con2.cursor(MySQLdb.cursors.DictCursor)
    cur2.execute("SELECT * FROM bywayexplorer_coordinate WHERE driveid = '" + driveid + "' ORDER BY routeOrder")
    coordinates = cur2.fetchall()
    cur.close()
    if con2:
      con2.close()
      
    drv = DBDrive()
    drv.driveid = coordinates[0]["driveid"]
    drv.startLat = coordinates[0]["latitude"]
    drv.startLon = coordinates[0]["longitude"]
    last = len(coordinates) - 1 
    drv.stopLat = coordinates[last]["latitude"]
    drv.stopLon = coordinates[last]["longitude"]
    con3 = getMySqlConnection("djangosite")
    cur3 = con3.cursor()
    print("UPDATE bywayexplorer_drive SET startLat=" + str(drv.startLat) + ", startLon=" + str(drv.startLon) + ", stopLat=" + str(drv.stopLat) + ", stopLon=" + str(drv.stopLon) + " WHERE driveid='" + str(drv.driveid) + "';")
    cur3.execute("UPDATE bywayexplorer_drive SET startLat=" + str(drv.startLat) + ", startLon=" + str(drv.startLon) + ", stopLat=" + str(drv.stopLat) + ", stopLon=" + str(drv.stopLon) + " WHERE driveid='" + str(drv.driveid) + "'"  )
    con3.commit
    cur3.close()
    if con3:
      con3.close()
    
except MySQLdb.Error, e:
  print "Error %d: %s" % (e.args[0],e.args[1])
  sys.exit(1)
