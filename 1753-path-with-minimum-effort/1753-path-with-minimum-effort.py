class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m,n =len(heights),len(heights[0])
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        heap=[(0,0,0)]
        efforts=[[float('inf')]*n for _ in range(m)]
        efforts[0][0]=0
        while heap:
            effort,r,c=heappop(heap)
            if r==m-1 and c==n-1:
                return effort
            for dr,dc in directions:
                new_r,new_c=r+dr,c+dc
                if 0<=new_r<m and 0<=new_c<n:
                    new_effort=max(effort,abs(heights[new_r][new_c]-heights[r][c]))
                    if new_effort<efforts[new_r][new_c]:
                        efforts[new_r][new_c]=new_effort
                        heappush(heap,(new_effort,new_r,new_c))
        return -1