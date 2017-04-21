import _mysql

class Database(object):
	
	def __init__(self, host, port, user, passwd, db):
		self.host = host
		self.port = port
		self.user = user
		self.passwd = passwd
		self.db = db

	def connect(self):
		self.__db = _mysql.connect(host=self.host,port=self.port,user=self.user,passwd=self.passwd,db=self.db)

	def query(self, query_string, row_limit = 50):
		self.__db.query(query_string)
		r = self.__db.use_result()

		return r.fetch_row(row_limit, 1)

	def close(self):
		self.__db.close()

		return 0