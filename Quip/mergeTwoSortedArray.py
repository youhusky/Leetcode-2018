def merge(a,b):
	# T O(max(m,n))
	res = []
	m,n = len(a), len(b)
	i,j = 0,0
	# O(min(m,n))
	while i < m and j < n:
		if a[i] < b[j]:
			res.append(a[i])
			i += 1
		else:
			res.append(b[j])
			j += 1
	print (i,j)
	# O(abs(m-n))
	if i == m:
		res += b[j:]
	elif j == n:
		res += a[i:]
	return res

a = [1,2,3]
b = [1,3,4]
print(merge(a,b))