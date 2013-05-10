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
