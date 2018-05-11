def minSubArrayLen(nums, target):
	if not nums:
		return 0
	l, r = 0,0
	minlength = len(nums)+1
	res = 0
	while r < len(nums):
		res += nums[r]
		r += 1
		while res >= target:
			minlength = min(minlength, r-l)
			res -= nums[l]
			l += 1
	return 0 if minlength == len(nums)+1 else minlength

print minSubArrayLen([2,3,1,2,4,3],7)