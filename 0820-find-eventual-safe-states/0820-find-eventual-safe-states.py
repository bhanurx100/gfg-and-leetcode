class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        unvisited=0
        visited=1
        safe=2
        def dfs(node:int)->bool:
            if state[node]!=unvisited:
                return state[node]==safe
            state[node]=visited
            for neighbor in graph[node]:
                if state[neighbor]==safe:
                    continue
                if state[neighbor]==visited or not dfs(neighbor):
                    return False
            state[node]=safe
            return True
        state=[unvisited]*len(graph)
        safe_nodes=[node for node in range(len(graph)) if dfs(node)]
        return safe_nodes