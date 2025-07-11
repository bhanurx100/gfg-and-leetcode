import heapq
class Solution:
    def mostBooked(self,n: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        free = list(range(n))          # min‑heap by room index
        heapq.heapify(free)

        busy = []                      # (endTime, room)
        count = [0] * n

        for s, e in meetings:
            # release rooms
            while busy and busy[0][0] <= s:
                _, r = heapq.heappop(busy)
                heapq.heappush(free, r)

            if free:
                r = heapq.heappop(free)
                new_end = e
            else:
                end_time, r = heapq.heappop(busy)
                new_end = end_time + (e - s)
            heapq.heappush(busy, (new_end, r))
            count[r] += 1

        return max(range(n), key=count.__getitem__)