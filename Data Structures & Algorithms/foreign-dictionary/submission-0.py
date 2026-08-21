class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        graph=collections.defaultdict(set)

        for word in words:
            for ch in word:
                graph[ord(ch)-ord('a')]

        for i in range(1,len(words)):

            word1=words[i-1]
            word2=words[i]

            minLen=min(len(word1),len(word2))

            if len(word1)>len(word2) and word1[:minLen]==word2:
                return ""

            for ind in range(minLen):
                if word1[ind]!=word2[ind]:
                    graph[ord(word1[ind])-ord('a')].add(ord(word2[ind])-ord('a'))
                    break
        topo=self.topoSort(graph)
        

        if len(topo)!=len(graph):
            return ""
        return "".join(chr(node + ord('a')) for node in topo)
    
    def topoSort(self,graph):

        indegree=[0]*26

        for node in graph.keys():
            for neighbor in graph[node]:
                indegree[neighbor]+=1
        
        dq=collections.deque()

        for node in graph:
            if indegree[node]==0:
                dq.append(node)
        
        topo=[]

        while dq:

            node=dq.popleft()
            topo.append(node)

            for neighbor in graph[node]:
                indegree[neighbor]-=1

                if indegree[neighbor]==0:
                    dq.append(neighbor)
        return topo