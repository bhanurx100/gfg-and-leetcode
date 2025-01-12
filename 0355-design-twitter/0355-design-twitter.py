from collections import defaultdict
import heapq

class Twitter:
    def __init__(self):
        self.time = 0  # Global timestamp to order tweets
        self.tweets = defaultdict(list)  # userId -> list of (timestamp, tweetId)
        self.following = defaultdict(set)  # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Append tweet with timestamp to user's tweet list
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1  # Increment timestamp

    def getNewsFeed(self, userId: int) -> list:
        heap = []  # Max-heap to store recent tweets
        
        # Ensure user follows themselves
        self.following[userId].add(userId)
        
        # Gather recent tweets from user and followees
        for followee in self.following[userId]:
            for time, tweetId in self.tweets[followee][-10:]:  # Only consider the last 10 tweets for efficiency
                heapq.heappush(heap, (-time, tweetId))  # Use -time for max-heap
        
        # Extract up to 10 most recent tweets
        news_feed = []
        while heap and len(news_feed) < 10:
            news_feed.append(heapq.heappop(heap)[1])
        
        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        # Follower starts following followee
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Follower unfollows followee (cannot unfollow themselves)
        if followeeId != followerId:
            self.following[followerId].discard(followeeId)
