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
  i = 0
  for driveRow in driveRows:
    driveid = driveRow[0]
    newDrive = DBDrive()
    newDrive.driveid = driveRow[0]
    newDrive.driveName = driveRow[1]
    print newDrive.toString()
    i += 1
    if (i > 5):
      break;
except sqlite3.Error, e:
  print "Error %d: %s" % (e.args[0],e.args[1])
  sys.exit(1)
finally:
  if con:
    con.close() 

    
  


