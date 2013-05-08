import abc

class DBObject(object):
	__metaclass__ = abc.ABCMeta

  	@abc.abstractmethod
 	def getColumns(self):
 		raise NotImplementedError, "Please override in derived class"
	
	@abc.abstractmethod
 	def getTableName(self):
 		raise NotImplementedError, "Please override in derived class" 		

