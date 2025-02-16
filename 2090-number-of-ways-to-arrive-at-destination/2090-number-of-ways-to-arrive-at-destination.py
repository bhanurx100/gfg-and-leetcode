from heapq import heappop, heappush
from collections import defaultdict
from typing import List

MOD = 10**9 + 7  # To avoid overflow

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # Step 1: Create adjacency list {node: [(neighbor, weight), ...]}
        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # Step 2: Initialize Dijkstra's Algorithm
        min_heap = [(0, 0)]  # (distance, node)
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1

        while min_heap:
            time, node = heappop(min_heap)

            # If we already found a shorter path to this node, skip
            if time > dist[node]:
                continue

            # Step 3: Process neighbors
            for neighbor, travel_time in graph[node]:
                new_time = time + travel_time

                # Found a shorter path to neighbor
                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    ways[neighbor] = ways[node]  # Reset ways to this path
                    heappush(min_heap, (new_time, neighbor))

                # Found another shortest path (same distance)
                elif new_time == dist[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD  # Add paths

        return ways[n-1] % MOD  # Answer: Number of ways to reach node (n-1)
