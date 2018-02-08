class Solution:
    def splitListToParts(self, root, k):
        total_len = 0
        head = root
        while head:
            total_len += 1
            head = head.next
        
        ans = [None for _ in range(k)]
        
        l, r = total_len / k, total_len % k
        
        prev, head = None, root
        
        for i in range(k):
            ans[i] = head
            for j in range(l + (1 if r > 0 else 0)):
                prev, head = head, head.next
            if prev: 
                prev.next = None
            # only for first round
            r -= 1
        
        return ans
