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
  coord = DBCoord()
  cur.execute("SELECT * FROM " + coord.getTableName())
  coordRows = cur.fetchall()
  for coord in coordRows:
    
    newCoord = DBCoordinate()
    newCoord.driveid = coord[0]
    newCoord.routeOrder = coord[1]
    newCoord.latitude = coord[2]
    newCoord.longitude = coord[3]
    newCoord.insertIntoMySQLDB("djangosite","bywayexplorer_coordinate")
except sqlite3.Error, e:
  print "Error %d: %s" % (e.args[0],e.args[1])
  sys.exit(1)
finally:
  if con:
    con.close() 
