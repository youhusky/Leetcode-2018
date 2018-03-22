#
# [224] Basic Calculator
#
# https://leetcode.com/problems/basic-calculator/description/
#
# algorithms
# Hard (28.53%)
# Total Accepted:    64K
# Total Submissions: 224.4K
# Testcase Example:  '"1 + 1"'
#
# Implement a basic calculator to evaluate a simple expression string.
# 
# The expression string may contain open ( and closing parentheses ), the plus
# + or minus sign -, non-negative integers and empty spaces  .
# 
# You may assume that the given expression is always valid.
# 
# Some examples:
# 
# "1 + 1" = 2
# " 2-1 + 2 " = 3
# "(1+(4+5+2)-3)+(6+8)" = 23
# 
# 
# 
# 
# Note: Do not use the eval built-in library function.
# 
#
class Solution(object):
    def calculate(self, s):
        res, num, sign, stack = 0, 0, 1, []
        for i in s:
            if i.isdigit():
                num = 10*num + int(i)
            elif i == "+":
                res += num * sign 
                num = 0
                sign = 1 
            elif i == '-':
                res += num*sign
                num = 0
                sign = -1
            elif i == "(":
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif i == ")":
                res += num * sign
                res *= stack.pop()
                res += stack.pop()
                num = 0
        if num != 0:
            res += sign * num
        return res

