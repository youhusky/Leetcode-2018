class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.backtracking(nums, res, [],0)
        return res
    
    def backtracking(self, nums, res, temp,start):
        res.append(list(temp))
        for i in range(start, len(nums)):
            temp.append(nums[i])
            self.backtracking(nums, res, temp, i+1)
            temp.pop()
