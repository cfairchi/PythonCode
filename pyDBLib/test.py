#!/usr/bin/python
# _*_ coding: utf-8 _*_

import sqlite3 as lite
import sys
import DBObject
from DBDrive import DBDrive
import sqliteDBUtils 

		
drive = DBDrive()
drive.createSQLiteTable("BywayExplorer.db",True)

