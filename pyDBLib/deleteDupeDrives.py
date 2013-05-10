#!/usr/bin/python
# _*_ coding: utf-8 _*_


import sys
import os
import MySQLdb

from DBDrive import DBDrive
from chrispwd import getUserName
from chrispwd import getPassword

def getMySqlConnection(self, theDBName):
  return MySQLdb.Connection(user=getUserName(), passwd=getPassword(), db=theDBName, host='localhost')

con = getMySqlConnection("djangosite")

try:
  driveIds = []
  cur = con.cursor(mdb.cursors.DictCursor)
  cur.execute("SELECT * from FROM bywayexplorer_drive ORDER BY driveid")
  driveRows = cur.fetchall()
  i = 0
  for drive in driveRows:
    if (drive["driveid"] in driveIds):
      print("Duplicate: " + drive["id"] + " -- " + drive["driveid"])
    else:
      driveIds.append(drive["driveid"])
      
    i += 1
    if (i > 5):
      break
    
    
