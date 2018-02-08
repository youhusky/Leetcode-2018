class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.backtracking(nums, [], res)
        return res
    def backtracking(self, nums, temp, ans):
        if len(nums) == len(temp): # quit loop
            ans.append(list(temp))
        for i in range(len(nums)):
            if nums[i] in temp: # cut duplicate
                continue
            temp.append(nums[i])
            
            self.backtracking(nums, temp, ans)
            temp.pop()

