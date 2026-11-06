
class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:

        logs.sort(key=lambda a: a[1])

        q = sorted((t, i) for i, t in enumerate(queries))

        count = {}
        ans = [0] * len(queries)

        left = 0
        right = 0

        for time, idx in q:

            # Add logs within the current time range
            while right < len(logs) and logs[right][1] <= time:
                server = logs[right][0]
                count[server] = count.get(server, 0) + 1
                right += 1

            # Remove logs outside the current time range
            while left < right and logs[left][1] < time - x:
                server = logs[left][0]
                count[server] -= 1

                if count[server] == 0:
                    del count[server]

                left += 1

            ans[idx] = n - len(count)

        return ans
