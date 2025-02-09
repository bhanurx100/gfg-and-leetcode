class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        in_degree=[0]*numCourses
        for dest,src in prerequisites:
            graph[src].append(dest)
            in_degree[dest]+=1
        queue=deque([i for i in range(numCourses) if in_degree[i]==0])
        topo_order=[]
        while queue:
            vertex=queue.popleft()
            topo_order.append(vertex)
            for neighbor in graph[vertex]:
                in_degree[neighbor]-=1
                if in_degree[neighbor]==0:
                    queue.append(neighbor)
        if len(topo_order)==numCourses:
            return topo_order
        else:
            return []