class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.backtracking(n,k,res,[], 1)
        return res
    def backtracking(self,n,k,res,temp,start):
        if k == 0:
            res.append(list(temp))
        for i in range(start, n+1):
            temp.append(i)
            self.backtracking(n,k-1,res,temp,i+1)
            temp.pop()
        
