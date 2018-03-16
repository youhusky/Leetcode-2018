#
# [127] Word Ladder
#
# https://leetcode.com/problems/word-ladder/description/
#
# algorithms
# Medium (19.96%)
# Total Accepted:    157.6K
# Total Submissions: 789.4K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 
# Given two words (beginWord and endWord), and a dictionary's word list, find
# the length of shortest transformation sequence from beginWord to endWord,
# such that:
# 
# 
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
# 
# 
# 
# For example,
# 
# 
# Given:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# 
# As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
# 
# 
# 
# Note:
# 
# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# 
# 
# 
# 
# UPDATE (2017/1/20):
# The wordList parameter had been changed to a list of strings (instead of a
# set of strings). Please reload the code definition to get the latest changes.
# 
#
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if not beginWord or not endWord or not wordList:
            return 0
        if endWord not in wordList:
            return 0
        count = 0
        
        wordList = set(wordList)
        
        begin, end = set(), set()
        begin.add(beginWord)
        end.add(endWord)
        
        while begin and end:
            if len(begin) > len(end):
                begin, end = end, begin
            count += 1
            # to store next set
            nextSet = set()
            for each in begin:
                for i in range(len(each)):
                    for j in range(26):
                        # not the same
                        if chr(97+j) != each[i]:
                            temp = each[:i] + chr(97+j) + each[i+1:]
                            # we find
                            if temp in wordList:
                                wordList.remove(temp)
                                nextSet.add(temp)
                            
                            if temp in end:
                                return count + 1
            begin = nextSet
        return 0
                            
