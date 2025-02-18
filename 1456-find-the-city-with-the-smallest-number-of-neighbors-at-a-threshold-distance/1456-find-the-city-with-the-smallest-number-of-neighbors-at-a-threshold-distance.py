class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        INF=10**8
        dist=[[INF]*n for _ in range(n)]
        for i in range(n):
            dist[i][i]=0
        for u,v,w in edges:
            dist[u][v]=w
            dist[v][u]=w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k]<INF and dist[k][j]<INF:
                        dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
        min_reachable=n
        best_city=-1
        for i in range(n):
            reachable_cities=sum(1 for j in range(n) if i!=j and dist[i][j]<=distanceThreshold)
            if reachable_cities<min_reachable or (reachable_cities==min_reachable and i>best_city):
                min_reachable=reachable_cities
                best_city=i
        return best_city