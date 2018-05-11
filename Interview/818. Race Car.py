def racecar(n):
	# corner case
	if n == 0:
		return 0

	visit = set((0,1))
	queue = [[0,1]]
	count = 0

	while queue:
		newqueue = []
		# update
		count += 1

		# iterate every candidate
		for index, speed in queue:
			index1, speed1 = index + speed, speed * 2
			index2, speed2 = index, -1 if speed > 0 else 1

			if index1 == n:
				return count
			newqueue.append((index1, speed1))
			if (index2, speed2) not in visit:
				visit.add((index2, speed2))
				newqueue.append((index2, speed2))

		queue = newqueue
	return -1
print racecar(6)