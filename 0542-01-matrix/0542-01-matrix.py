class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows,cols=len(mat),len(mat[0])
        queue=deque()
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        for r in range(rows):
            for c in range(cols):
                if mat[r][c]==0:
                    queue.append((r,c,0))
                else:
                    mat[r][c]=-1
        while queue:
            r,c,dist=queue.popleft()
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if 0<=nr<rows and 0<=nc<cols and mat[nr][nc]==-1:
                    mat[nr][nc]=dist+1
                    queue.append((nr,nc,dist+1))
        return mat