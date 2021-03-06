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
con.autocommit(True);

try:
  cur = con.cursor(MySQLdb.cursors.DictCursor)
  cur.execute("SELECT driveid FROM bywayexplorer_drive")
  drives = cur.fetchall()
  cur.close()
  i = 0
  dCount = 0
  for drive in drives:
    #print("Drive: " + drive["driveid"] + " Item: " + str(dCount) + " of " + str(len(drives)))
    dCount+=1;
    coords = []
    cur = con.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM bywayexplorer_coordinate WHERE driveid ='" + drive["driveid"] + "' ORDER BY routeOrder")
    coordinates = cur.fetchall()
    cur.close()
    for coord in coordinates:
      coordString = coord["driveid"]+str(coord["latitude"])+str(coord["longitude"])
      if (coordString in coords):
        i+=1
        cur = con.cursor()
        sql = "DELETE FROM bywayexplorer_coordinate WHERE id = " + str(coord["id"]) 
        print(sql)
        cur.execute(sql)
        
        
        #print("Duplicate:(" + str(i) + ") " + str(coord["id"]) + "," + coord["driveid"] + "," + str(coord["latitude"]) + "," + str(coord["longitude"]))
      else:
        coords.append(coordString)
      
except MySQLdb.Error, e:
  print "Error %d: %s" % (e.args[0],e.args[1])
  sys.exit(1)
finally:
  if con:
    con.close() 
