import heapq
def findbicycle(people, bicycle):
	# list of list

	def calcualte_distance(a, b):
		# list of points
		return abs(a[0]- b[0]) *  abs(a[0]- b[0]) +  abs(a[1]- b[1])* abs(a[1]- b[1])
	queue = []
	bicycle_set = set()
	person_set = set()
	for person in people:
		for bic in bicycle:
			heapq.heappush(queue, (calcualte_distance(person,bic), tuple(person),tuple(bic)))

	res = []
	while queue:
		distance, person, bic = heapq.heappop(queue)

		if person in person_set or bic in bicycle_set:
			continue
		res.append([person, bic])
		bicycle_set.add(bic)
		person_set.add(person)
	return res
peopletest = [[1,1],[2,2],[1,3]]
bicycletest = [[1,2],[3,1],[3,3]]
print findbicycle(peopletest,bicycletest)