class CountSquares:

    def __init__(self):
        self.points=[]
        self.pointCount={}
        
    def add(self, point: List[int]) -> None:
        self.points.append(point)
        self.pointCount[tuple(point)]=self.pointCount.get(tuple(point),0)+1
        
    def count(self, point: List[int]) -> int:

        x1,y1=point
        res=0

        for x2,y2 in self.points:

            if abs(x1-x2)==abs(y1-y2) and (x1-x2)!=0 and (y1-y2)!=0:
                res+=(self.pointCount.get((x1,y2),0)*self.pointCount.get((x2,y1),0))
        return res
        
