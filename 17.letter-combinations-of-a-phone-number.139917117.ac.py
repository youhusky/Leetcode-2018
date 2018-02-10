#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (36.00%)
# Total Accepted:    212.9K
# Total Submissions: 591.2K
# Testcase Example:  '""'
#
# Given a digit string, return all possible letter combinations that the number
# could represent.
# 
# 
# 
# A mapping of digit to letters (just like on the telephone buttons) is given
# below.
# 
# 
# 
# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
# 
# 
# Note:
# Although the above answer is in lexicographical order, your answer could be
# in any order you want.
# 
#
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        self.backtracking(digits, res, dic, "", 0)
        return res
    def backtracking(self, digits, res, dic, temp, index):
        # corner
        if len(temp) == len(digits):
            res.append(temp)
            return
        for char in dic[digits[index]]:
            self.backtracking(digits, res, dic, temp+char, index+1)
            
        
        
