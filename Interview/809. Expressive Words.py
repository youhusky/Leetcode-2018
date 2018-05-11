class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        count = 0
        for word in words:
            i,j = 0,0
            while i != len(S) and j != len(word):
                if S[i] != word[j]:
                    break
                c1, c2 = 0,0
                while i + c1 < len(S) and S[i] == S[i+c1]:
                    c1 += 1
                while j + c2 < len(word) and word[j] == word[j+c2]:
                    c2 += 1
                if c1 < c2 or c1 < 3 and c1 != c2:
                    break
                i += c1
                j += c2
            if i == len(S) and j == len(word):
                count += 1
        return count