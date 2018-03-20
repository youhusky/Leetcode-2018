#
# [599] Minimum Index Sum of Two Lists
#
# https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/
#
# algorithms
# Easy (46.46%)
# Total Accepted:    27.9K
# Total Submissions: 60K
# Testcase Example:  '["Shogun","Tapioca Express","Burger King","KFC"]\n["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]'
#
# 
# Suppose Andy and Doris want to choose a restaurant for dinner, and they both
# have a list of favorite restaurants represented by strings. 
# 
# 
# You need to help them find out their common interest with the least list
# index sum. If there is a choice tie between answers, output all of them with
# no order requirement. You could assume there always exists an answer.
# 
# 
# 
# Example 1:
# 
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".
# 
# 
# 
# Example 2:
# 
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["KFC", "Shogun", "Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is
# "Shogun" with index sum 1 (0+1).
# 
# 
# 
# 
# Note:
# 
# The length of both lists will be in the range of [1, 1000].
# The length of strings in both lists will be in the range of [1, 30].
# The index is starting from 0 to the list length minus 1.
# No duplicates in both lists.
# 
# 
#
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dic1, dic2 = dict(), dict()
        res_index = len(list1) + len(list2)
        for i, s in enumerate(list1):
            dic1[s] = i
            
        for i, s in enumerate(list2):
            if s in dic1:
                temp = i + dic1[s]
                dic2[temp] = dic2.get(temp,[]) + [s]
                res_index = min(res_index, temp)
        return dic2[res_index]
      
