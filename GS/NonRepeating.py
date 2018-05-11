def getCharArray(strs):
	count = [0] * 256
	for i in strs:
		count[ord(i)]+=1
	return count

def NonRepeating(strs):
	# abcdf - a
	# racecars - e
	#count = getCharArray(strs)
	count = dict()
	for s in strs:
		count[s] = count.get(s,0)+1

	for s in strs:
		if count[s] == 1:
			return s
	
	# for s in strs:
	# 	if count[ord(s)] == 1:
	# 		return s
	# return -1

print NonRepeating("abcdf")
	