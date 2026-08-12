class Twitter:

    def __init__(self):

        self.followingMap=[set() for _ in range(500)]
        self.tweetsMap=collections.defaultdict(list)
        self.time=0
        

    def postTweet(self, userId: int, tweetId: int) -> None:

        self.tweetsMap[userId].append((self.time,tweetId))
        self.time+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:

        heap=[]

        def addTweets(userId):

            for time,tweet in self.tweetsMap[userId]:

                if len(heap)<10:
                    heapq.heappush(heap,(time,tweet))
                elif heap[0][0]<time:
                    heapq.heappushpop(heap,(time,tweet))
        
        addTweets(userId)

        for following in self.followingMap[userId]:
            if following!=userId:
                addTweets(following)
        
        heap.sort(key = lambda x:x[0],reverse=True)
        return [tweet for time,tweet in heap]
        

        

    def follow(self, followerId: int, followeeId: int) -> None:

        self.followingMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followingMap[followerId].discard(followeeId)
        
