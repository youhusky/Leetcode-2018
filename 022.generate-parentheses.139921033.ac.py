class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n < 1:
            return []
        res = []
        self.backtracking(n, res, "", 0, 0)
        return res
    def backtracking(self,n, res, temp, left, right):
        if left < n:
            self.backtracking(n, res, temp + '(' , left+1, right)
        if right < left:
            self.backtracking(n ,res, temp + ')', left, right+1)
        if right == n:
            res.append(temp)
        
