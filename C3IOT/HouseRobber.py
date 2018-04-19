# DP S O(n)
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])   
        return dp[-1]

# DP S O(1)        
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        
        first = nums[0]
        second = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            third = max(first + nums[i], second)
            first = second
            second = third
        return second
        
# Rob2
# T O(n)
# S O(1)
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0
        if len(nums) < 2:
            return nums[0]
        return max(self.rob_helper(nums,0,len(nums)-1), self.rob_helper(nums, 1, len(nums)))
    
    def rob_helper(self, nums, start, end):
        if start == 0:
            first = nums[0]
            second = max(nums[0], nums[1])
        else:
            first = 0
            second = nums[1]
        for i in range(2, end):
            third = max(first + nums[i], second)
            first = second
            second = third
        return second
            