#
# [808] Number of Matching Subsequences
#
# https://leetcode.com/problems/number-of-matching-subsequences/description/
#
# algorithms
# Medium (24.80%)
# Total Accepted:    947
# Total Submissions: 3.8K
# Testcase Example:  '"abcde"\n["a","bb","acd","ace"]'
#
# Given string S and a dictionary of words words, find the number of words[i]
# that is a subsequence of S.
# 
# 
# Example :
# Input: 
# S = "abcde"
# words = ["a", "bb", "acd", "ace"]
# Output: 3
# Explanation: There are three words in words that are a subsequence of S: "a",
# "acd", "ace".
# 
# 
# Note:
# 
# 
# All words in words and S will only consists of lowercase letters.
# The length of S will be in the range of [1, 50000].
# The length of words will be in the range of [1, 5000].
# The length of words[i] will be in the range of [1, 50].
# 
#
class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        res = 0
        dic = collections.defaultdict(list)
        for word in words:
            dic[word[0]].append(word)
        
        for s in S:
            queue = dic[s]
            size = len(queue)
            for i in range(size):
                word = queue.pop(0)
                if len(word) == 1:
                    res += 1
                    continue
                word = word[1:]
                dic[word[0]].append(word)
                
        return res
