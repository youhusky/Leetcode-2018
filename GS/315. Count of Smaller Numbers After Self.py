class Solution(object):
    def countSmaller(self, nums):
        counts = []
        done = []
        for num in nums[::-1]:
            #counts.insert(0, bisect.bisect_left(done, num))
            counts.append(self.binarysearch(done, num))
            l = self.binarysearch(done, num)
            done = done[:l] +[num] + done[l:]
            #bisect.insort(done, num)
            
        return counts[::-1]
        
    def binarysearch(self, done, num):
        l,r = 0 ,len(done)
        while l  < r:
            mid = (r+l)/2
            if done[mid] < num:
                l = mid+1
            else:
                r = mid
        return l