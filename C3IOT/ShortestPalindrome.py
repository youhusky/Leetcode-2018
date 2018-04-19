class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def reverseString(s):
	        r = list(s)
	        i, j  = 0, len(r) - 1
	        while i < j:
	            r[i], r[j] = r[j], r[i]
	            i += 1
	            j -= 1

	        return "".join(r)

	     def reverseString(s):
	     	return s[::-1]


        rev = s[::-1]
        j = 0
        # comare abcbaddd
        #        dddabcba
        for i in range(len(s)):
        	# i == 3
            if s[:len(s) - i] == rev[i:]:
                return rev[:i] + s
        return ""

# O(n^2)
# O (n)
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        j = len(s)-1
        end = j
        
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                i = 0
                end -= 1
                j = end
        return s[end+1:][::-1] + s

# dp[i][j] = substring(i,j) 范围内，构造 palindrome 的最小编辑次数
# 如果 s[i] == s[j]
# dp[i][j] = dp[i + 1][j - 1] (不需要操作)
# 同时考虑 i , j 相邻的情况
# 如果 s[i] != s[j]，那么我们可以经 add/delete 操作构造出当前的 s(i, j)
# s(i + 1, j) + ADD
# s(i, j - 1) + ADD
def MinInsertionsForPalindrome(s):
	n = len(s)
	dp = [[0 for _ in range(n)] for _ in range(n)]
	diff = 0
	while diff < n:
		for i in range(n-diff):
			j = i + diff
			if i == j:
				dp[i][j] = 0
			elif s[i] == s[j]:
				dp[i][j] = dp[i+1][j-1]
			else:
				dp[i][j] = 1 + min(dp[i][j-1], dp[i+1][j])
		diff += 1
	return dp[0][-1]        
        