#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sqlite3 as lite
import sys
import DBObject
from DBDrive import DBDrive
import xml.etree.ElementTree as ET
		
drive = DBDrive()
drive.createSQLiteTable("BywayExplorer.db",True)
tree = ET.parse("byways.xml")
elem = tree.getroot()
byways = elem.findall("Byway")
for byway in byways:
	drive = DBDrive()
	drive.id = byway.find("id").text
	drive.
