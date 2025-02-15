class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph=defaultdict(list)
        for u,v,cost in flights:
            graph[u].append((v,cost))
        heap=[(0,src,k+1)]
        best_cost={}
        while heap:
            cost,node,stops=heappop(heap)
            if node==dst:
                return cost
            if stops>0:
                for neighbor,price in graph[node]:
                    new_cost=cost+price
                    if (neighbor,stops-1)not in best_cost or new_cost<best_cost[(neighbor,stops-1)]:
                        best_cost[(neighbor, stops - 1)] = new_cost
                        heappush(heap, (new_cost, neighbor, stops - 1))
        
        return -1 