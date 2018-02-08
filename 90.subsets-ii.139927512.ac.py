class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        self.backtracking(nums, res, [],0)
        return res
    
    def backtracking(self, nums, res, temp,start):
        res.append(list(temp))
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            temp.append(nums[i])
            self.backtracking(nums, res, temp, i+1)
            temp.pop()
        
