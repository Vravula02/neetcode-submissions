class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans=[]

        hash={}

        for str in strs:
            key=tuple(sorted(str))
            if key in hash:
                hash[key].append(str)
            else:
                hash[key]=[str]
        
        for val in hash.values():
            ans.append(val)
        
        return ans
        
        