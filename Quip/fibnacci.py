def fibnacci(N):
	#O(2^n)
	if N == 1:
		return 1
	elif N == 2:
		return 1
	else:
		return fibnacci(N - 1) + fibnacci(N - 2)
print (fibnacci(5))

def fibnacci2(n):
	# O(n), O(n)
	if n <=2:
		return 1
	dp = [0 for _ in range(n+1)]
	dp[1]= 1
	dp[2] = 1
	dp[3] = 1
	for i in range(4, n+1):
		dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
	return dp[-1]

print(fibnacci2(10))

def fibnacci3(n):
	# O(n), O(1)
	if n <=3:
		return 1
	first, second, third = 1,1,1
	for i in range(4, n+1):
		temp = first+second+third
		first = second
		second = third
		third = temp
	return third
print fibnacci3(6)


