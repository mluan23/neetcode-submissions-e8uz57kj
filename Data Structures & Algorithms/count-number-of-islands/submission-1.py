class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands  = 0
        m = len(grid)
        n = len(grid[0])
        seen = set()

        def dfs(grid, i, j, seen):
            m = len(grid)
            n = len(grid[0])
            if i >= m or i < 0 or j >= n or j < 0:
                return 
            if grid[i][j] == '0':
                return
            if (i,j) in seen:
                return
            seen.add((i, j))
            dfs(grid, i+1, j, seen)
            dfs(grid, i-1, j, seen)
            dfs(grid, i, j+1, seen)
            dfs(grid, i, j-1, seen)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in seen:
                    num_islands += 1
                    dfs(grid, i, j, seen)
        return num_islands