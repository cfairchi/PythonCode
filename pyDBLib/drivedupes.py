#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
import os
import MySQLdb

from DBDrive import DBDrive
from chrispwd import getUserName
from chrispwd import getPassword

def getMySqlConnection(theDBName):
	return MySQLdb.Connection(user=getUserName(), passwd=getPassword(), db=theDBName, host='localhost')

con = getMySqlConnection("djangosite")

try:
	driveIds = []
	cur = con.cursor(MySQLdb.cursors.DictCursor)
	cur2 = con.cursor()
	cur.execute("SELECT * FROM bywayexplorer_drive ORDER BY driveid")
	driveRows = cur.fetchall()
	for drive in driveRows:
		if (drive["driveid"] in driveIds):
			cur2.execute("DELETE FROM bywayexplorer_drive WHERE id = " + str(drive["id"]))
			con.commit()
			print("Duplicate: " + str(drive["id"]) + " -- " + drive["driveid"])
		else:
			driveIds.append(drive["driveid"])
      
except MySQLdb.Error, e:
	print "Error %d: %s" % (e.args[0],e.args[1])
	sys.exit(1)
finally:
	if con:
		con.close() 
