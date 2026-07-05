class MedianFinder:

    def __init__(self):
        self.mn=[]
        self.mx=[]
        

    def addNum(self, num: int) -> None:
        
        if self.mx and -self.mx[0]<num:
            heapq.heappush(self.mn,num)
        else:
            heapq.heappush(self.mx,-num)
        
        if len(self.mn)>len(self.mx):
            heapq.heappush(self.mx,-heapq.heappop(self.mn))
        
        if len(self.mx)>len(self.mn)+1:
            heapq.heappush(self.mn,-heapq.heappop(self.mx))

    def findMedian(self) -> float:

        if len(self.mn)==len(self.mx)==0:
            return 0.0

        if len(self.mn)==len(self.mx):
            return (self.mn[0]-self.mx[0])/2
        
        return -self.mx[0]
        
        