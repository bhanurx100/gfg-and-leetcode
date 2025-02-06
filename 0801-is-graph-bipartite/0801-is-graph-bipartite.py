class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color={}
        def dfs(node:int)->bool:
            for neighbor in graph[node]:
                if neighbor in color:
                    if color[neighbor]==color[node]:
                        return False
                else:
                    color[neighbor]=1-color[node]
                    if not dfs(neighbor):
                        return False
            return True
        for node in range(len(graph)):
            if node not in color:
                color[node]=0
                if not dfs(node):
                    return False
        return True