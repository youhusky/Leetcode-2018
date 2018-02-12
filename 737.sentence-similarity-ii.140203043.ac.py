#
# [737] Sentence Similarity II
#
# https://leetcode.com/problems/sentence-similarity-ii/description/
#
# algorithms
# Medium (41.74%)
# Total Accepted:    5K
# Total Submissions: 12K
# Testcase Example:  '["great","acting","skills"]\n["fine","drama","talent"]\n[["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]'
#
# Given two sentences words1, words2 (each represented as an array of strings),
# and a list of similar word pairs pairs, determine if two sentences are
# similar.
# 
# For example, words1 = ["great", "acting", "skills"] and words2 = ["fine",
# "drama", "talent"] are similar, if the similar word pairs are pairs =
# [["great", "good"], ["fine", "good"], 
# ⁠["acting","drama"], ["skills","talent"]].
# 
# Note that the similarity relation is transitive. For example, if "great" and
# "good" are similar, and "fine" and "good" are similar, then "great" and
# "fine" are similar.
# 
# Similarity is also symmetric.  For example, "great" and "fine" being similar
# is the same as "fine" and "great" being similar.
# 
# Also, a word is always similar with itself.  For example, the sentences
# words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though
# there are no specified similar word pairs.
# 
# Finally, sentences can only be similar if they have the same number of
# words.  So a sentence like words1 = ["great"] can never be similar to words2
# = ["doubleplus","good"].
# 
# 
# Note:
# The length of words1 and words2 will not exceed 1000.
# The length of pairs will not exceed 2000.
# The length of each pairs[i] will be 2.
# The length of each words[i] and pairs[i][j] will be in the range [1, 20].
# 
#
class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        # O(n+m), O(n)
        # corner case
        if len(words1) != len(words2):
            return False
        # init
        group = {}
        for p1, p2 in pairs:
            root1 = self.find(p1, group)
            root2 = self.find(p2, group)
            if root1 == root2:
                pass
            else:
                group[root2] = root1
                
        # check
        m = len(words1)
        for i in range(m):
            root1 = self.find(words1[i], group)
            root2 = self.find(words2[i], group)
            if root1 == root2:
                pass
            else:
                return False
        return True
                
        
        
    def find(self, e, group):
        if e not in group:
            return e
        else:
            return self.find(group[e], group)
