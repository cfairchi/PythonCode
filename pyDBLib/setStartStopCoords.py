#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
import os
import MySQLdb

from DBDrive import DBDrive
from DBCoordinate import DBCoordinate
from chrispwd import getUserName
from chrispwd import getPassword

def getMySqlConnection(self, theDBName):
  return MySQLdb.Connection(user=getUserName(), passwd=getPassword(), db=theDBName, host='localhost')

con = getMySqlConnection("djangosite")

try:
  totalRequests = 0
  cur = con.cursor()
  coord = DBCoordinate()
  cur.execute("SELECT driveid FROM bywayexplorer_drive")
  driveRows = cur.fetchall()
  for drive in driveRows:
    driveid = drive[0]
    cur2 = con.cursor()
    cur2.execute("SELECT * FROM bywayexplorer_coordinate WHERE driveid = '" + driveid + "' ORDER BY routeOrder")
    coordinates = cur2.fetchall()
    drv = DBDrive()
    drv.driveid = coordinates[0][0]
    drv.startLat = coordinates[0][2]
    drv.startLon = coordinates[0][3]
    last = len(coordinates) - 1 
    drv.stopLat = coordinates[last][2]
    drv.stopLon = coordinates[last][3]
    cur3 = con.cursor()
    cur3.execute("UPDATE bywayexplorer_drive SET startLat=" + drv.startLat + ", startLon=" + drv.startLon + ", stopLat=" + drv.stopLat + ", stopLon=" + drv.stopLon + " WHERE driveid='" + drv.driveid + "'"  )
    cur3.commit
    
except sqlite3.Error, e:
  print "Error %d: %s" % (e.args[0],e.args[1])
  sys.exit(1)
finally:
  if con:
    con.close() 
