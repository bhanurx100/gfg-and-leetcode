class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                if board[r][c]!='.':
                    val=board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    box_index=(r//3)*3+(c//3)
                    boxes[box_index].add(val)
        def backtrack(r,c):
            if  c==9:
                return backtrack(r+1,0)
            if r==9:
                return True
            if board[r][c]!='.':
                return backtrack(r,c+1)
            for num in map(str,range(1,10)):
                box_index=(r//3)*3+(c//3)
                if num not in rows[r] and num not in cols[c] and num not in boxes[box_index]:
                    board[r][c]=num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_index].add(num)
                    if backtrack(r,c+1):
                        return True
                    board[r][c]='.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_index].remove(num)
            return False
        backtrack(0,0)