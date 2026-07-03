class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq={}

        for task in tasks:
            freq[task]=freq.get(task,0)+1
        
        maxFreq=0
        maxFreqCount=0

        for val in freq.values():
            if maxFreq<val:
                maxFreqCount=1
                maxFreq=val
            elif maxFreq==val: 
                maxFreqCount+=1

        blocks=maxFreq-1
        blockSize=n+1
        total=(blocks*blockSize)+maxFreqCount

        return max(len(tasks),total)


        