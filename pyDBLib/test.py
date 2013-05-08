#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sqlite3 as lite
import sys
import DBObject
from DBDrive import DBDrive

def createTable(theDBObject,theDatabase,theDeleteIfExists):
	con = None
	try:
		con = lite.connect('BywayExplorer.db')
		cur = con.cursor()
 		if (theDeleteIfExists):
			cur.execute("DROP TABLE IF EXISTS " + theDBObject.getTableName())
		sqlCmd = "CREATE TABLE "
		sqlCmd = sqlCmd + theDBObject.getTableName() + "("
		i = 0
		colNames = theDBObject.getColumns()
		for col in colNames:
			if (i !=0 ):
				sqlCmd = sqlCmd + "," + col + " TEXT"
			else:
				sqlCmd = sqlCmd + col + " TEXT"
		sqlCmd = sqlCmd + ")"
		cur.execute(sqlCmd)
		print("Table " + theDBObject.getTableName() + " Created")
		con.commit()
	except lite.Error, e:
		if con:
			con.rollback()
			print "Error %s:" % e.args[0]
			sys.exit(1)
	finally:
		if con:
			con.close()
		
drive = DBDrive()
createTable(drive,"BywayExplorer.db",True)

