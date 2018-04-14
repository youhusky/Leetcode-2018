#
# [187] Repeated DNA Sequences
#
# https://leetcode.com/problems/repeated-dna-sequences/description/
#
# algorithms
# Medium (33.04%)
# Total Accepted:    93.7K
# Total Submissions: 283.6K
# Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
#
# 
# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
# for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to
# identify repeated sequences within the DNA.
# 
# Write a function to find all the 10-letter-long sequences (substrings) that
# occur more than once in a DNA molecule.
# 
# 
# For example,
# 
# Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
# 
# Return:
# ["AAAAACCCCC", "CCCCCAAAAA"].
# 
#
class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        dictionary = dict()
        temp = []
        for x in range(len(s) - 9):
            temp.append(s[x : x + 10] )
        for i in temp:
            dictionary[i] = dictionary.get(i, 0) + 1
        return [k for k, v in dictionary.iteritems() if v > 1]
