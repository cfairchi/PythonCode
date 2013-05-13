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
conn.autocommit(True);

try:
	cur = con.cursor()
	liteCon = lite.connect('BywayExplorer_First.db')
	liteCur = liteCon.cursor()
	liteCur.execute("SELECT * from bywayexplorer_drive")
	liteDrives = liteCur.fetchall()

	for driveRow in liteDrives:
		short = driveRow[8]
		longD = driveRow[9]

		cur.execute("UPDATE bywayexplorer_drive SET shortDescription = %s WHERE driveid = %s", (short, driveRow[0]))    
	    print drv.driveid + " Number of rows updated: %d" % cur.rowcount
        cur.execute("UPDATE bywayexplorer_drive SET longDescription = %s WHERE driveid = %s", (longD, driveRow[0]))        
        print drv.driveid + " Number of rows updated: %d" % cur.rowcount 

except MySQLdb.Error, e:
  print "Error %d: %s" % (e.args[0],e.args[1])
  sys.exit(1)
finally:
  if con:
    con.close() 
