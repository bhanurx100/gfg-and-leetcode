class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        min_heap=[(0,k)]
        dist={}
        while min_heap:
            time,node=heappop(min_heap)
            if node in dist:
                continue
            dist[node]=time
            for neighbor,travel_time in graph[node]:
                if neighbor not in dist:
                    heappush(min_heap,(time+travel_time,neighbor))
        return max(dist.values())if len(dist)==n else -1