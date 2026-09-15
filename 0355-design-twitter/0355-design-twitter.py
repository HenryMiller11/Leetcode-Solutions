from typing import List
import heapq


class Twitter:

    def __init__(self):
        self.following = {}   # user -> set of followees
        self.tweets = {}      # user -> list of (time, tweetId)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # User's own tweets + tweets of followed users
        users = {userId}
        users.update(self.following.get(userId, set()))

        # Max heap:
        # (-time, tweetId, user, index)
        heap = []

        for user in users:
            if user in self.tweets and self.tweets[user]:
                index = len(self.tweets[user]) - 1
                time, tweetId = self.tweets[user][index]

                heapq.heappush(
                    heap,
                    (-time, tweetId, user, index)
                )

        result = []

        while heap and len(result) < 10:
            _, tweetId, user, index = heapq.heappop(heap)
            result.append(tweetId)

            # Move to the previous tweet of this user
            index -= 1

            if index >= 0:
                time, nextTweetId = self.tweets[user][index]

                heapq.heappush(
                    heap,
                    (-time, nextTweetId, user, index)
                )

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)