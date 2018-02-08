class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        used = [False for _ in range(len(nums))]
        self.backtracking(nums, res, used,[])
        return res
    def backtracking(self, nums, res, used,temp):
        if len(temp) == len(nums):
            res.append(list(temp))
            return
        for i in range(len(nums)):
            if used[i] or i>0 and nums[i]== nums[i-1] and not used[i-1]:
                continue
            temp.append(nums[i])
            used[i] = True
            self.backtracking(nums, res, used, temp)
            used[i] = False
            temp.pop()
            
        
