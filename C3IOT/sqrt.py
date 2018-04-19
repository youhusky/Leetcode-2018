def sqrt(n):
	l = 1.0
	h = n
	while h-l >0.01:
		mid = l + (h-l)/2
		if mid *mid - n > 0.01:
			h = mid
		else:
			l = mid
	return str(l)[:5]
print sqrt(2)