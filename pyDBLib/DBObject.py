import abc

class DBObject(object):
	__metaclass__ = abc.ABCMeta

  	@abc.abstractmethod
 	def getColumns(self):
 		raise NotImplementedError, "Please override in derived class"
	
	@abc.abstractmethod
 	def getTableName(self):
 		raise NotImplementedError, "Please override in derived class" 		

	def createSQLiteTable(theSQLiteDatabaseName,theDeleteIfExists):
		con = None
		try:
			con = lite.connect(theSQLiteDatabaseName)
			cur = con.cursor()
			if (theDeleteIfExists):
				cur.execute("DROP TABLE IF EXISTS " + getTableName())
			sqlCmd = "CREATE TABLE " + getTableName() + "("
			i = 0
			colNames = getColumns()
			for col in colNames:
				if (i !=0 ):
					sqlCmd = sqlCmd + "," + col + " TEXT"
				else:
					sqlCmd = sqlCmd + col + " TEXT"
			sqlCmd = sqlCmd + ")"
			cur.execute(sqlCmd)
			print("Table " + getTableName() + " Created")
			con.commit()
		except lite.Error, e:
			if con:
				con.rollback()
				print "Error %s:" % e.args[0]
				sys.exit(1)
		finally:
			if con:
				con.close()
