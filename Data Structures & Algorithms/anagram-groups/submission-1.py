class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sortedStrs=defaultdict(list)

        for s in strs:
            key="".join(sorted(s))
            sortedStrs[key].append(s)

        
        return list(sortedStrs.values())