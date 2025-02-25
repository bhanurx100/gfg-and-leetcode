from typing import List

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # Step 1: Build the adjacency list
        adj = [[] for _ in range(n)]
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
        
        # Step 2: Initialize discovery time and lowest reachable time arrays
        disc = [-1] * n  # Discovery time of nodes
        low = [-1] * n   # Lowest discovery time reachable from this node
        bridges = []     # List to store critical connections
        time = 0         # Global time counter

        # Step 3: DFS function
        def dfs(node, parent):
            nonlocal time
            disc[node] = low[node] = time  # Set discovery and low time
            time += 1
            
            for neighbor in adj[node]:
                if neighbor == parent:  # Ignore the parent node
                    continue
                if disc[neighbor] == -1:  # If neighbor is unvisited
                    dfs(neighbor, node)
                    # Update low-link value
                    low[node] = min(low[node], low[neighbor])
                    
                    # If the lowest reachable time of the neighbor is greater, it's a bridge
                    if low[neighbor] > disc[node]:
                        bridges.append([node, neighbor])
                else:
                    # Back edge (Cycle), update low-link value
                    low[node] = min(low[node], disc[neighbor])
        
        # Step 4: Run DFS from node 0 (assuming the graph is connected)
        dfs(0, -1)

        return bridges
