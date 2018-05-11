def helper(nums, target, temp, res, start):
	if target == 0:
		res.append(list(temp))
	if target < 0:
		return
	for i in range(start, len(nums)):
		temp.append(nums[i])
		helper(nums, target - nums[i], temp, res, i)
		temp.pop()

def targetSum(nums, target):
	res = []
	helper(nums, target, [],res, 0)
	return res

print targetSum([1,2,3],6)
