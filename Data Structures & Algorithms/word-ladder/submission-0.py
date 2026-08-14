class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        

        words=set(wordList)
        words.discard(beginWord)

        if endWord not in words:
            return 0
        
        dq=collections.deque()

        dq.append((beginWord,1))

        while dq:

            word,steps=dq.popleft()

            if word==endWord:
                return steps

            for i in range(len(word)):
                for ch in range(ord('a'),ord('z')+1):
                    newWord=word[:i]+chr(ch)+word[i+1:]
                    if newWord in words:
                        dq.append((newWord,steps+1))
                        words.discard(newWord)
        return 0

