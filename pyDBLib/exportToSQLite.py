#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
import os
import MySQLdb
import sqlite3 as lite
import sys
import DBObject
import urllib2
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
  cur = con.cursor(MySQLdb.cursors.DictCursor)
  cur.execute("SELECT * FROM bywayexplorer_drive")
  driveRows = cur.fetchall()
  
  liteCon = lite.connect('BywayExplorer.db')
  liteCur = liteCon.cursor()
  tempDrive = DBDrive()
  tempDrive.createSQLiteTable("BywayExplorer.db",True)
  
  for driveRow in driveRows:
    drive = DBDrive()
    drive.setValues(driveRow)
    
  
except MySQLdb.Error, e:
  print "Error %d: %s" % (e.args[0],e.args[1])
  sys.exit(1)
finally:
  if con:
    con.close() 
