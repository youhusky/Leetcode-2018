class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.count = 0
        self.queue = []

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        if not self.queue or self.queue[-1][0] != timestamp:
            self.queue.append([timestamp,1])
        else:
            self.queue[-1][1] += 1
        self.count += 1
        
    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        # move forward
        while self.queue and timestamp - self.queue[0][0] >= 300:
            self.count -= self.queue.pop(0)[1]
        return self.count


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)