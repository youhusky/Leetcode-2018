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