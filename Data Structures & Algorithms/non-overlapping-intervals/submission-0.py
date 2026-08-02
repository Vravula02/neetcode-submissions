class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        n=len(intervals)

        count=1

        intervals.sort(key= lambda x:x[1])
        latestEnd=intervals[0][1]

        for i in range(1,n):

            if latestEnd<=intervals[i][0]:
                count+=1
                latestEnd=intervals[i][1]
        return n-count