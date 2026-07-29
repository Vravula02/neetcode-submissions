class Solution:

    def encode(self, strs: List[str]) -> str:

        length=[]
        
        for s in strs:
            length.append(len(s))
        
        res=""
        i=0

        while i<len(strs):
            res+=str(length[i])
            res+="#"
            res+=strs[i]
            i+=1
        
        return res

    def decode(self, s: str) -> List[str]:

        res=[]

        i=0

        while i<len(s):

            j=i

            while s[j]!="#":
                j+=1
            length=int(s[i:j])

            word=s[j+1:j+1+length]
            res.append(word)
            i=j+1+length
                  
        return res
