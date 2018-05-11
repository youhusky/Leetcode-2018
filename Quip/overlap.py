from collections import defaultdict
test =  [(1, 1), (3, 3)], [(2, 2), (4, 4)], [(1, 3), (2, 4)], [(2, 2), (3, 3)]
x = defaultdict(list)
y = []
for i in range(len(test)):
	# rec
	x[test[i][0][0]].append(chr(i))
	x[test[i][1][0]].append(chr(i))
	y.append([test[i][0][1], chr(i)])
	y.append([test[i][1][1], chr(i)])
y = sorted(y)
print y
total = 0
for line in sorted(x.keys()):
	candidate = x[line]
	count = 0
	s =set()
	for val in y:
		if val[1] in candidate:
			if val[1] in s:
				break
			else:
				count += 1
				
				s.add(val[1])
				total = max(total, count)
print total