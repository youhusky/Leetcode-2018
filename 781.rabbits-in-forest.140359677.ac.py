#
# [797] Rabbits in Forest
#
# https://leetcode.com/problems/rabbits-in-forest/description/
#
# algorithms
# Medium (46.41%)
# Total Accepted:    1.7K
# Total Submissions: 3.6K
# Testcase Example:  '[1,0,1,0,0]'
#
# In a forest, each rabbit has some color. Some subset of rabbits (possibly all
# of them) tell you how many other rabbits have the same color as them. Those
# answers are placed in an array.
# 
# Return the minimum number of rabbits that could be in the forest.
# 
# 
# Examples:
# Input: answers = [1, 1, 2]
# Output: 5
# Explanation:
# The two rabbits that answered "1" could both be the same color, say red.
# The rabbit than answered "2" can't be red or the answers would be
# inconsistent.
# Say the rabbit that answered "2" was blue.
# Then there should be 2 other blue rabbits in the forest that didn't answer
# into the array.
# The smallest possible number of rabbits in the forest is therefore 5: 3 that
# answered plus 2 that didn't.
# 
# Input: answers = [10, 10, 10]
# Output: 11
# 
# Input: answers = []
# Output: 0
# 
# 
# Note:
# 
# 
# answers will have length at most 1000.
# Each answers[i] will be an integer in the range [0, 999].
# 
# 
#
class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        if not answers:
            return 0
        dic = {}
        count = 0
        for each in answers:
            if each not in dic:
                dic[each] = each
                count += 1 
            else:
                if dic[each] == 0:
                    dic[each] = each
                    count += 1 
                else:
                    dic[each] -= 1
                    count +=1
            
        for value in dic.values():
            count += value
        
        return count
