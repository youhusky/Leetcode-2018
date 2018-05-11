class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0 ,len(nums)-1
        # init check
        if nums[l] < nums[r]:
            return nums[l]
        
        while l + 1 < r:
            mid = l + (r-l) /2
            # l always index to the larger one
            if nums[r] > nums[mid]:
                r = mid
            else:
                l = mid
        return min(nums[r], nums[l])

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l, r = 0 ,len(nums)-1
        if nums[l] < nums[r]:
            return nums[l]
        while l + 1 < r:
            mid = l + (r-l)/2
            if nums[mid] == nums[r]:
                r -= 1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                l = mid
        return min(nums[l], nums[r])
        