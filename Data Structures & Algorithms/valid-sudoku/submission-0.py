class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in rows[row]:
                    return False
                rows[row].add(board[row][col])
                if board[row][col] in cols[col]:
                    return False
                cols[col].add(board[row][col])

                square = (row // 3 ) * 3 + (col // 3 )
                if board[row][col] in squares[square]:
                    return False
                squares[square].add(board[row][col])
        return True 
                
