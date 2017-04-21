from util.database import Database
from util.excel import Excel

def main():
	spreadsheet('data.xlsx')
	db()

def spreadsheet(fileName):
	print 'Retrieving from spreadsheets'

	wb = Excel(fileName)
	wb.open()
	data = wb.retrieve()

	print data[0]['id_value']
	print data[0]['name']

def db():
	print 'Retrieving from database...'

	# connects to a mysql db
	db = Database('172.17.0.2',3306,'root','test-pass','mysql')
	db.connect()

	# retrieves a hash table of data from sql
	data = db.query('SELECT * FROM People')

	print data[0]['id_value']
	print data[0]['name']

	db.close()
	print 'Database connection closed'

main()