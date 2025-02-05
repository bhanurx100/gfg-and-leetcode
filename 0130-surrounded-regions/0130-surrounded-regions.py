class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return 
        rows,cols=len(board),len(board[0])
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or board[r][c]!='O':
                return 
            board[r][c]='#'
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        for r in range(rows):
            for c in [0,cols-1]:
                if board[r][c]=='O':
                    dfs(r,c)
        for c in range(cols):
            for r in [0,rows-1]:
                if board[r][c]=='O':
                    dfs(r,c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='O':
                    board[r][c]='X'
                elif board[r][c]=='#':
                    board[r][c]='O'

