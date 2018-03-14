#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (26.66%)
# Total Accepted:    140.4K
# Total Submissions: 526.7K
# Testcase Example:  '"a"\n"a"'
#
# 
# Given a string S and a string T, find the minimum window in S which will
# contain all the characters in T in complexity O(n).
# 
# 
# 
# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
# 
# 
# Minimum window is "BANC".
# 
# 
# 
# Note:
# If there is no such window in S that covers all characters in T, return the
# empty string "".
# 
# 
# If there are multiple such windows, you are guaranteed that there will always
# be only one unique minimum window in S.
# 
#
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # sliding windows
        if not s or not t:
            return ""
        res = ""
        dic = dict()
        # init
        for char in t:
            dic[char] = dic.get(char, 0) + 1
        l,r = 0, 0
        minLength = len(s)
        # windows
        size = len(t)
        
        while r < len(s):
            if s[r] in dic:
                # duplicate-- dic value maybe < 0
                if dic[s[r]] > 0:
                    size -= 1
                    
                dic[s[r]] -= 1
            
            # windos
            r += 1
            
            while size == 0:
                if minLength >= r-l:
                    minLength = r-l
                    res = s[l:r]
                    #t = [l :r]
                    
                # left bound
                if s[l] in dic:
                    dic[s[l]] += 1
                    if dic[s[l]] > 0:
                        size += 1
                l += 1
        return res
                
            
