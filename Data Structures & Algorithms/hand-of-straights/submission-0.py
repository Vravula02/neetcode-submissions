class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        n=len(hand)

        if n%groupSize!=0:
            return False
        
        freq={}

        for card in hand:
            freq[card]=freq.get(card,0)+1
        
        for card in sorted(freq):
            
            count=freq[card]

            if count>0:
                for i in range(1,groupSize):
                    nextCard=card+i
                    if nextCard not in freq or freq[nextCard]<count:
                        return False
                    freq[nextCard]-=count
        return True