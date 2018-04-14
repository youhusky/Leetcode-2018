#
# [282] Expression Add Operators
#
# https://leetcode.com/problems/expression-add-operators/description/
#
# algorithms
# Hard (30.61%)
# Total Accepted:    46.3K
# Total Submissions: 151.3K
# Testcase Example:  '"123"\n6'
#
# 
# Given a string that contains only digits 0-9 and a target value, return all
# possibilities to add binary operators (not unary) +, -, or * between the
# digits so they evaluate to the target value.
# 
# 
# Examples: 
# "123", 6 -> ["1+2+3", "1*2*3"] 
# "232", 8 -> ["2*3+2", "2+3*2"]
# "105", 5 -> ["1*0+5","10-5"]
# "00", 0 -> ["0+0", "0-0", "0*0"]
# "3456237490", 9191 -> []
# 
# 
# Credits:Special thanks to @davidtan1890 for adding this problem and creating
# all test cases.
#
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.res = []
        self.target = target
        self.helper(num, "", 0, 0)
        return self.res
    
    def helper(self, num, temp, curSum, prevNum):
        if not num:
            if curSum == self.target:
                self.res.append(temp)
                return
        # split range(1..len(num))
        for i in range(1, len(num)+1):
            # deal with "00..
            curString = num[:i]
            if len(curString) > 1 and curString[0] == '0':
                return
            curNum = int(curString)
            # index start from 1
            nextString = num[i:]
            if len(temp) > 0:
                self.helper(nextString, temp + '+' + curString, curSum + curNum, curNum)
                self.helper(nextString, temp + '-' + curString, curSum - curNum, -curNum)
                self.helper(nextString, temp + '*' + curString, (curSum - prevNum) + prevNum * curNum, prevNum * curNum)
                
            else:
                self.helper(nextString, curString, curNum, curNum)
        
        
