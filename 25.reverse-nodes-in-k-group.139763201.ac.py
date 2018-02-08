class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverse(self, start, end):
        
        prev=ListNode(0)
        prev.next=start
        while prev.next!=end:
            tmp=start.next
            start.next=tmp.next
            tmp.next=prev.next
            prev.next=tmp
        return [end, start]
    
    def reverseKGroup(self, head, k):
        if head==None: 
            return None
        dummy=ListNode(0)
        dummy.next=head
        start=dummy
        while start.next:
            end=start
            for i in range(k-1):
                end=end.next
                if end.next==None: 
                    return dummy.next
            res=self.reverse(start.next, end.next)
            start.next=res[0]
            start=res[1]
        return dummy.next
