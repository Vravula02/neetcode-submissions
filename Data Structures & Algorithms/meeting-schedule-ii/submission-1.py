"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        n=len(intervals)
        intervals.sort(key=lambda x:x.start)
        pq=[]
        ans=0

        for interval in intervals:
            if pq and pq[0]<=interval.start:
                heapq.heappushpop(pq,interval.end)
            else:
                heapq.heappush(pq,interval.end)
            ans=max(ans,len(pq))
        return ans

        