class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m,n=len(grid),len(grid[0])
        visited=[[False]*n for _ in range(m)]
        def dfs(x,y):
            if x<0 or x>=m or y<0 or y>=n:
                return 0
            if visited[x][y] or grid[x][y]<=0:
                return 0
                
            visited[x][y]=True
            total=grid[x][y]
            # for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            total+=dfs(x+1,y)
            total+=dfs(x-1,y)
            total+=dfs(x,y+1)
            total+=dfs(x,y-1)
               
            return total
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]>0 and not visited[i][j]:
                    sums=dfs(i,j)
                    if sums%k==0:
                        count+=1
        return count