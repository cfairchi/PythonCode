import abc
import sqlite3
import MySQLdb
import sys
import os

lib_path = os.path.abspath('../')
sys.path.append(lib_path)

from chrispwd import getUserName
from chrispwd import getPassword


class DBObject(object):
	__metaclass__ = abc.ABCMeta

  	@abc.abstractmethod
 	def getColumns(self):
 		raise NotImplementedError, "Please override in derived class"
	
	@abc.abstractmethod
 	def getTableName(self):
 		raise NotImplementedError, "Please override in derived class"
 		
 	@abc.abstractmethod
 	def toString(self):
 		raise NotImplementedError, "Please override in derived class"
 		
 	@abc.abstractmethod
 	def getValues(self):
 		raise NotImplementedError, "Please override in derived class" 		

	def getMySqlConnection(self, theDBName):
		
		#return _mysql.connect('localhost',getUserName(),getPassword(),theDBName)
		return MySQLdb.Connection(user=getUserName(), passwd=getPassword(), db=theDBName, host='localhost')
		
	
	def insertIntoMySQLDB(self, theDBName, theTableName):
		con = None
		try:
			con = self.getMySqlConnection(theDBName)
			cur = con.cursor()
			values = self.getValues()
			colNames = self.getColumns()
			colString = "("
			valString = "("
			
			i = 0
			for col in colNames:
				if (i > 0):
					colString += ","
					valString += ","

				colString += col[0]
					
				if (col[1] == "INT"):
					valString += values[col[0]]
				else:
					valString += "'" + values[col[0]] + "'"
				i += 1
					
			colString += ")"
			valString += ")"
			print("INSERT INTO " + theTableName + " " + colString + " " +  valString)
			cur.execute("INSERT INTO " + theTableName + " " + colString + " " +  valString)
				
			
		except MySQLdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])
    			sys.exit(1)
		finally:
			if con:
        			con.close()
			
			
	def insertIntoSQLiteDB(self, theSQLiteDatabaseName):
		con = None
		try:
			con = sqlite3.connect(theSQLiteDatabaseName)
			cur = con.cursor()
			values = self.getValues()
			colNames = self.getColumns()
			valString = " VALUES("
			colIndex = 0
	        	for col in colNames:
	        		if (colIndex > 0):
	        			valString = valString + ","
	        		if (col[1] == "INT"):
					valString = valString + str(values[col[0]]).replace("'","''")
				else:
	        			valString = valString + "'" + values[col[0]].replace("'","''") + "'"
				colIndex = colIndex + 1
	        	valString = valString + ")"
			
			#print("INSERT INTO " + self.getTableName() + valString)
			cur.execute("INSERT INTO " + self.getTableName() + valString)
			con.commit()
	   	except sqlite3.Error, e:
	        	if con:
		            con.rollback()
		            print "Error %s:" % e.args[0]
	        	    sys.exit(1)
		finally:
	        	if con:
				con.close()
	
		
	def createSQLiteTable(self,theSQLiteDatabaseName,theDeleteIfExists):
	    con = None
	    try:
	        con = sqlite3.connect(theSQLiteDatabaseName)
	        cur = con.cursor()
	        if (theDeleteIfExists):
	            cur.execute("DROP TABLE IF EXISTS " + self.getTableName())
	        sqlCmd = "CREATE TABLE " + self.getTableName() + "("
	        i = 0
	        colNames = self.getColumns()
	        for col in colNames:
	            if (i !=0 ):
	                sqlCmd = sqlCmd + "," + col[0] + " " + col[1]
	            else:
	                sqlCmd = sqlCmd + col[0] + " " + col[1]
		    i +=1;
	        sqlCmd = sqlCmd + ")"
		print(sqlCmd)
	        cur.execute(sqlCmd)
	        print("Table " + self.getTableName() + " Created")
	        con.commit()
	    except sqlite3.Error, e:
	        if con:
	            con.rollback()
	            print "Error %s:" % e.args[0]
	            sys.exit(1)
	    finally:
	        if con:
			con.close()
