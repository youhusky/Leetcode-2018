#
# [140] Word Break II
#
# https://leetcode.com/problems/word-break-ii/description/
#
# algorithms
# Hard (24.40%)
# Total Accepted:    110.1K
# Total Submissions: 451.1K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# 
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, add spaces in s to construct a sentence where each word is a
# valid dictionary word. You may assume the dictionary does not contain
# duplicate words.
# 
# 
# 
# Return all such possible sentences.
# 
# 
# 
# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].
# 
# 
# 
# A solution is ["cats and dog", "cat sand dog"].
# 
# 
# 
# UPDATE (2017/1/4):
# The wordDict parameter had been changed to a list of strings (instead of a
# set of strings). Please reload the code definition to get the latest changes.
# 
#
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        # O（2^n）
        return self.helper(s, wordDict, {})

    def helper(self, s, wordDict, memo):
        if s in memo: 
            return memo[s]
        if not s: return []

        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
                #print resultOfTheRest
                for item in resultOfTheRest:
                    item = word + ' ' + item
                    res.append(item)
                #print res,s
        memo[s] = res
        return res
        
        
