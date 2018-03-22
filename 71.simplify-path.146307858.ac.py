#
# [71] Simplify Path
#
# https://leetcode.com/problems/simplify-path/description/
#
# algorithms
# Medium (26.25%)
# Total Accepted:    109.9K
# Total Submissions: 418.8K
# Testcase Example:  '"/"'
#
# Given an absolute path for a file (Unix-style), simplify it.
# 
# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# 
# 
# click to show corner cases.
# 
# Corner Cases:
# 
# 
# 
# Did you consider the case where path = "/../"?
# In this case, you should return "/".
# Another corner case is the path might contain multiple slashes '/' together,
# such as "/home//foo/".
# In this case, you should ignore redundant slashes and return "/home/foo".
# 
# 
#
class Solution(object):
    def simplifyPath(self, path):
        stack = []
        for p in path.split("/"):
            if p == "..":
                if stack: 
                    stack.pop()
            elif p and p != '.': 
                stack.append(p)
        return "/" + "/".join(stack)
        
