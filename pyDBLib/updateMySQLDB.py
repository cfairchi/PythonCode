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
con.autocommit(True);

try:
	cur = con.cursor()
	
	liteCon = lite.connect('bywayexplorer_current.db')
	liteCon.row_factory = lite.Row
	liteCur = liteCon.cursor()
	liteCur.execute("SELECT * FROM drives")
	liteDrives = liteCur.fetchall()

	for driveRow in liteDrives:
		cur.execute("UPDATE bywayexplorer_drive SET region = %s WHERE driveid = %s", (driveRow["region"], driveRow["id"]))    
		print driveRow["id"] + " Number of rows updated: %d" % cur.rowcount
		cur.execute("UPDATE bywayexplorer_drive SET restrictions = %s WHERE driveid = %s", (driveRow["restrictions"], driveRow["id"]))    
		print driveRow["id"] + " Number of rows updated: %d" % cur.rowcount
	    	cur.execute("UPDATE bywayexplorer_drive SET seasons = %s WHERE driveid = %s", (driveRow["seasons"], driveRow["id"]))        
    		print driveRow["id"] + " Number of rows updated: %d" % cur.rowcount 
		cur.execute("UPDATE bywayexplorer_drive SET considerations = %s WHERE driveid = %s", (driveRow["considerations"], driveRow["id"]))        
	    	print driveRow["id"] + " Number of rows updated: %d" % cur.rowcount 
    		cur.execute("UPDATE bywayexplorer_drive SET directions = %s WHERE driveid = %s", (driveRow["directions"], driveRow["id"]))        
    		print driveRow["id"] + " Number of rows updated: %d" % cur.rowcount 


except MySQLdb.Error, e:
  print "Error %d: %s" % (e.args[0],e.args[1])
  sys.exit(1)
finally:
  if con:
    con.close() 
