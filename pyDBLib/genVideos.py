import sys
import os
import sqlite3
import DBDrive from DBDrive
import DBCoordinate from DBCoordinate

from csf_StreetView import generateVideoFromCoords

try:
  con = sqlite3.connect('BywayExplorer.db")
  cur = con.cursor()
  cur.execute("SELECT driveid FROM " + DBDrive.getTableName())
  driveRows = cur.fetchall()
  for driveRow in driveRows:
    driveid = driveRow[0]
    print ("SELECT * FROM " + DBCoordinate.getTableName() " + " WHERE driveid='" + driveid + "'")
    cur.execute("SELECT * FROM " + DBCoordinate.getTableName() " + " WHERE driveid='" + driveid + "'")
    coords = cur.fetchall()
    
    for coord in coords:
      lat = coord[2]
      lon = coord[3]
      alt = 0
    
  


