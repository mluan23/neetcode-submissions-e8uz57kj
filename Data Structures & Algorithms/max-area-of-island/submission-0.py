class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        self.count = 0
        max_=  0

        def dfs(grid, r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return
            if grid[r][c] == 0:
                return
            if (r,c) in seen:
                return
            else:
                seen.add((r,c))
                self.count += 1
                dfs(grid, r-1, c)
                dfs(grid, r+1, c)
                dfs(grid, r, c-1)
                dfs(grid, r, c+1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in seen and grid[i][j] == 1:
                    self.count = 0
                    dfs(grid, i, j)
                    max_ = max(max_, self.count)
        return max_

            