class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.backtrack(board[i][j], word, board, i, j, False, set()):
                    return True
        return False
    

    def backtrack(self, cur_word, word, board, row, col, res, visited):
        if (row, col) in visited:
            return
        if cur_word[-1] != word[len(cur_word) - 1]:
            return
        if cur_word == word:
            return True
        visited.add((row, col))
        if col + 1 < len(board[0]):
            res= res or self.backtrack(cur_word + board[row][col+1], word, board, row, col+1, res, visited)
        if col - 1 >= 0:
            res= res or self.backtrack(cur_word + board[row][col-1], word, board, row, col-1, res, visited)
        if row + 1 < len(board):
            res= res or self.backtrack(cur_word + board[row+1][col], word, board, row+1, col, res, visited)
        if row - 1 >= 0:
            res= res or self.backtrack(cur_word + board[row-1][col], word, board, row-1, col, res, visited)
        visited.remove((row, col))
        return res

