class Solution(object):
    def minmaxGasDist(self, stations, K):
        pq = [] #(-part_length, original_length, num_parts)
        for i in xrange(len(stations) - 1):
            x, y = stations[i], stations[i+1]
            heapq.heappush(pq,(x-y, y-x, 1))
        #heapq.heapify(pq)

        for _ in xrange(K):
            negnext, orig, parts = heapq.heappop(pq)
            parts += 1
            heapq.heappush(pq, (-(orig / float(parts)), orig, parts))

        return -pq[0][0]