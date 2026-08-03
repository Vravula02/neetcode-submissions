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
        
        startTime=[]
        endTime=[]

        for interval in intervals:
            startTime.append(interval.start)
            endTime.append(interval.end)
        
        startTime.sort()
        endTime.sort()

        count=0
        ans=0

        i,j=0,0

        while i<n and j<n:

            if startTime[i]<endTime[j]:
                count+=1
                i+=1
            else:
                j+=1
                count-=1
            ans=max(ans,count)
        return ans