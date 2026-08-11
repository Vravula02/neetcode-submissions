class TimeMap:

    def __init__(self):

        self.mpp={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key in self.mpp:
            self.mpp[key].append([value,timestamp])
        else:
            self.mpp[key]=[[value,timestamp]]
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.mpp:
            return ""
        
        lists=self.mpp[key]
        res=""

        low=0
        high=len(lists)-1

        while low<=high:

            mid=(low+high)//2

            if lists[mid][1]<=timestamp:
                res=lists[mid][0]
                low=mid+1
            else:
                high=mid-1
        return res