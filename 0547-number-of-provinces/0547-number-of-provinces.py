from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node):
            visited[node] = True
            for neighbor in range(len(isConnected)):
                if isConnected[node][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)
        
        n = len(isConnected)  # Number of nodes (cities)
        visited = [False] * n
        provinces = 0
        
        for i in range(n):
            if not visited[i]:  # If the city is not visited, it's a new province
                provinces += 1
                dfs(i)  # Start DFS from this city
        
        return provinces
