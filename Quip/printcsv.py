import csv
import sys
res = []
file = sys.argv[1]
with open(file) as f:
	#reader = csv.reader(f)
	# print reader
	# for row in reader:
	# 	print row
	f.seek(0)
	read = f.read(7)
	res.append(read)
print res[0].split(',')