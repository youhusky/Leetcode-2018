#
# [692] Top K Frequent Words
#
# https://leetcode.com/problems/top-k-frequent-words/description/
#
# algorithms
# Medium (41.29%)
# Total Accepted:    19.2K
# Total Submissions: 46.4K
# Testcase Example:  '["i", "love", "leetcode", "i", "love", "coding"]\n2'
#
# Given a non-empty list of words, return the k most frequent elements.
# Your answer should be sorted by frequency from highest to lowest. If two
# words have the same frequency, then the word with the lower alphabetical
# order comes first.
# 
# Example 1:
# 
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
# ⁠   Note that "i" comes before "love" due to a lower alphabetical order.
# 
# 
# 
# Example 2:
# 
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is",
# "is"], k = 4
# Output: ["the", "is", "sunny", "day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
# ⁠   with the number of occurrence being 4, 3, 2 and 1 respectively.
# 
# 
# 
# Note:
# 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Input words contain only lowercase letters.
# 
# 
# 
# Follow up:
# 
# Try to solve it in O(n log k) time and O(n) extra space.
# 
# 
#
import collections
import heapq

# min-heap
class Element:
    def __init__(self, word, count):
        self.count = count
        self.word = word
        
    def __lt__(self, other):
        if self.count == other.count:
            # reverse
            return self.word > other.word
        return self.count < other.count
    
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        counts = dict()
        for word in words:
            counts[word] = counts.get(word,0) + 1
        freqs = []
        for word, count in counts.items():
            heapq.heappush(freqs, Element(word, count))
            if len(freqs) > k:
                heapq.heappop(freqs)
        
        return [heapq.heappop(freqs).word for _ in xrange(len(freqs))][::-1]
