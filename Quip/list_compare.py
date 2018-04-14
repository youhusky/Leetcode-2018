# -*- coding: utf-8 -*-
# 1. 给你两个list of string，两个list里都各自没有duplicate，然后找到其中只在一个list里出现的string。问了时间空间复杂度。
# 比如：
# a = [1,2,3]
# b = [2,4,6]
# return: [1,3,4,6]

# 2. follow up 1：如果里面有duplicate呢。问了时间空间复杂度。
# 比如：. 1point3acres.com/bbs
# a = [1,2,3]
# b = [2,4,4,6]
# return: [1,3,4,6]

# 3. follow up 2：如果给你一个list of list of string，random size，怎么写。问了时间空间复杂度。（这儿我脑崩了……时间没想到，唉）. 1point 3acres 璁哄潧
# 比如：
# a = [1,2,3]
# b = [2,4,4,6]
# ...
# n = [x,x,x,x]
a = [1,2,3]
b = [2,4,6]
def origin(a,b):
	# T O(2(m + n))
	# S O(m + n)
	dic = dict()
	res = []
	for each in a+b:
		dic[each] = dic.get(each,0) + 1
	# without order
	for key in dic:
		if dic[key] == 1:
			res.append(key)

	# with order
	# for each in a+b:
	# 	if dic[each] == 1:
	# 		res.append(each)
	return res
print (origin(a,b))
a = [1,2,3]
b = [2,4,4,6]
def follow1(a,b):
	# T O(2(m + n))
	# S O(m + n)
	
	res = []
	dic = dict()
	for each in a:
		#if each not in dic:
		dic[each] = 0
		# else:
		# 	dic[each] = [dic[each][0] + 1, 'first']
	for each in b:
		if each not in dic:
			dic[each] = 1
		else:
			if dic[each] == -1:
				continue
			if dic[each] == 0:
				dic[each] = -1

	#print(dic)
	for key in dic:
		if dic[key] != -1:
			res.append(key)
	return res
print (follow1(a,b))

nums = [[1,2,3,4],[5,5,6,7,3],[8,9,1]]
def follow2(nums):
	# T O(mn)
	# S O(mn)
	dic = dict()
	res = []
	for i in range(len(nums)):
		for each in nums[i]:
			if each not in dic:
				dic[each] = i
			else:
				if dic[each] == -1:
					continue
				if dic[each] != i:
					dic[each] = -1
	#print (dic)
	for key in dic:
		if dic[key] != -1:
			res.append(key)
	return res
print(follow2(nums))
