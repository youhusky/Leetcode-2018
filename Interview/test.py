# name, city, address, age, city, zipCod
# a,b,cc,12,d,e
# ee,ff,bb,13,r,y
class CSVDataWarehouse(object):
	"""docstring for CSVDataWarehouse"""
	def __init__(self):
		super(CSVDataWarehouse, self).__init__()
		with open('test.csv') as f:
			data = f.readlines()
		self.output = data

	def getdata(self):
		return self.output

class CSVRecord(object):
	"""docstring for CSVRecord"""
	def __init__(self):
		super(CSVRecord, self).__init__()
		m = CSVDataWarehouse()
		self.data = m.getdata()
		print self.data

	def get(self, i):
		if i > len(self.data) -1:
			return None

		return self.data[i+1]

	def getColumn(self,column):
		res = []
		for each in range(len(self.data)):
			res.append(self.data[each][column])
		return res

	def getsize(self):
		return len(self.data) - 1

m = CSVRecord()


		


