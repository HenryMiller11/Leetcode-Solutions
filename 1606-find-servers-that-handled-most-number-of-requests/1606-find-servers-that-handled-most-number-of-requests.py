class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        import heapq

        available = list(range(k))
        busy = []
        count = [0] * k

        for i in range(len(arrival)):
            while busy and busy[0][0] <= arrival[i]:
                end, server = heapq.heappop(busy)
                available.append(server)

            available.sort()

            if not available:
                continue

            start = i % k

            pos = -1
            for j in range(len(available)):
                if available[j] >= start:
                    pos = j
                    break

            if pos == -1:
                pos = 0

            server = available.pop(pos)

            count[server] += 1
            heapq.heappush(busy, (arrival[i] + load[i], server))

        maximum = max(count)
        return [i for i in range(k) if count[i] == maximum]