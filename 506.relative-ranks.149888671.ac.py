#
# [506] Relative Ranks
#
# https://leetcode.com/problems/relative-ranks/description/
#
# algorithms
# Easy (46.88%)
# Total Accepted:    29.5K
# Total Submissions: 62.9K
# Testcase Example:  '[5,4,3,2,1]'
#
# 
# Given scores of N athletes, find their relative ranks and the people with the
# top three highest scores, who will be awarded medals: "Gold Medal", "Silver
# Medal" and "Bronze Medal".
# 
# Example 1:
# 
# Input: [5, 4, 3, 2, 1]
# Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
# Explanation: The first three athletes got the top three highest scores, so
# they got "Gold Medal", "Silver Medal" and "Bronze Medal". For the left two
# athletes, you just need to output their relative ranks according to their
# scores.
# 
# 
# 
# Note:
# 
# N is a positive integer and won't exceed 10,000.
# All the scores of athletes are guaranteed to be unique.
# 
# 
# 
#
class Solution(object):    
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        # return the rank index
        # replace rank index with medal

        sorted_nums = sorted(nums, reverse=True)
        dic = {}
        medal = {0: 'Gold Medal', 1: 'Silver Medal', 2: 'Bronze Medal'}
        for i, n in enumerate(sorted_nums):
            if i in medal:
                dic[n] = medal[i]
            else:
                dic[n] = str(i + 1)
        output = []
        for n in nums:
            output.append(dic[n])
        return output
