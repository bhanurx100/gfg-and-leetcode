class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        board=["."*n for _ in range(n)]
        leftrow=[0]*n
        upperdiagonal=[0]*(2*n-1)
        lowerdiagonal=[0]*(2*n-1)
        def backtrack(col):
            if col==n:
                res.append(board[:])
                return
            for row in range(n):
                if leftrow[row]==0 and lowerdiagonal[row+col]==0 and upperdiagonal[n-1+row-col]==0:
                    board[row]=board[row][:col]+ 'Q' + board[row][col+1:]
                    leftrow[row]=1
                    lowerdiagonal[row+col]=1
                    upperdiagonal[n-1+row-col]=1
                    backtrack(col+1)
                    board[row]=board[row][:col]+'.'+board[row][col+1:]
                    leftrow[row]=0
                    lowerdiagonal[row+col] =0
                    upperdiagonal[n-1+row-col]=0
        backtrack(0)
        return res
