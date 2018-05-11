class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        s = self.reverse(s, 0, len(s)-1)
        
        i, start = 0, 0
        while i < len(s):
            if s[i] == ' ':
                s = self.reverse(s, start, i-1)
                start = i + 1
            elif i == len(s)-1:
                s = self.reverse(s, start, i)
            i += 1
        
    
    def reverse(self,s, i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return s