#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sys
import os
import sqlite3
import DBDrive from DBDrive
import DBCoordinate from DBCoordinate


from csf_StreetView import generateVideoFromCoords

try:
  totalRequests = 0
  con = sqlite3.connect('BywayExplorer.db")
  cur = con.cursor()
  cur.execute("SELECT driveid FROM " + DBDrive.getTableName())
  driveRows = cur.fetchall()
  for driveRow in driveRows:
    driveid = driveRow[0]
    outFile = driveid + "_video")
    if (not os.path.exists(outFile)):
      coordList = []
      print ("SELECT * FROM " + DBCoordinate.getTableName() " + " WHERE driveid='" + driveid + "'")
      cur.execute("SELECT * FROM " + DBCoordinate.getTableName() " + " WHERE driveid='" + driveid + "'")
      coords = cur.fetchall()
    
      for coord in coords:
        lat = coord[2]
        lon = coord[3]
        coordList.append(lat + "," + lon + "," + 0)
        totalRequests = totalRequests + 1
      
      print( "Generating: " + outFile)
      generateVideoFromCoords(coordList,driveid + "_video")
      print( "Done Generating: " + outFile + " Total Requests:" + totalRequests)
    else:
      print( "File Already Exists: " + outFile)
        
      
    
  


