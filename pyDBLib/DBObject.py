import abc
import sqlite3

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
	                sqlCmd = sqlCmd + "," + col + " TEXT"
	            else:
	                sqlCmd = sqlCmd + col + " TEXT"
	        sqlCmd = sqlCmd + ")"
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
