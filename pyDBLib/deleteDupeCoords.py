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
  coords = []
  cur = con.cursor(mdb.cursors.DictCursor)
  cur.execute("SELECT * from FROM bywayexplorer_coordinate ORDER BY driveid")
  coordinates = cur.fetchall()
  i = 0
  for coord in coordinates:
    coordString = coord["driveid"]+coord["latitude"]+coord["longitude"]
    if (coordString in coords):
      print("Duplicate: " + coord[id] + "," + coord["driveid"] + "," + coord["latitude"] + "," + coord["longitude"])
    else:
      coords.append(coordString)
    i += 1
    if (i > 5):
      break
