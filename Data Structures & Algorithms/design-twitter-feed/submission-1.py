import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        self.followed = defaultdict(set)
        self.tweets = defaultdict(list)
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.counter, tweetId))
        self.counter += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        h = []
        for f in self.followed[userId] | {userId}:
            for count, tid in self.tweets[f][-10:]:
                heapq.heappush(h, (count, tid))
                if len(h) > 10:
                    heapq.heappop(h)
        return [tid for _, tid in sorted(h, reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followed[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followed[followerId].discard(followeeId)