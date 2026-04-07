class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not (i, j) in seen:
                    self.bfs(i, j, grid, seen)
                    count += 1
        return count


    def bfs(self, row, col, grid, seen):
        if grid[row][col] == '0':
            return
        seen.add((row, col))
        left = col - 1
        right = col + 1
        up = row - 1
        down = row + 1 

        if left >= 0 and grid[row][col-1] == '1' and not (row, col-1) in seen:
            self.bfs(row, col-1, grid, seen)
        if right < len(grid[0]) and grid[row][col+1] == '1' and not (row, col+1) in seen:
            self.bfs(row, col+1, grid, seen)
        if up >= 0 and grid[row-1][col] == '1' and not (row-1, col) in seen:
            self.bfs(row-1, col, grid, seen)
        if down < len(grid) and grid[row+1][col] == '1' and not (row+1, col) in seen:
            self.bfs(row+1, col, grid, seen)