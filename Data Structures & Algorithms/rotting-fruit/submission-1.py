class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # alright so we do multisource BFS
        # what that means if insert every rotten fruit into
        # the cell
        # keep track of the number of fresh fruits 
        # so we can track when none remain
        # keep track of a time
        num_fresh = 0
        queue = []
        seen = set()
        # if the queue is ever empty it means that we must
        # return -1
        def getNeighbors(row, col):
            neighbors = []
            left,right,up,down = col-1, col+1, row+1, row-1
            if left >= 0:
                neighbors.append((row, left))
            if right < len(grid[0]):
                neighbors.append((row, right))
            if down >= 0:
                neighbors.append((down, col))
            if up < len(grid):
                neighbors.append((up, col))
            return neighbors

                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    num_fresh += 1
                if grid[i][j] == 2:
                    queue.append((i,j))
                    seen.add((i,j))
        if num_fresh == 0:
            return 0
        # alright so we've added in all the multiple sources
        # now what? we can run bfs
        # after we run bfs, we just check num fruit is 0 or not
        time = 0
        while queue:
            if num_fresh == 0: return time
            
            time += 1
            # we need to get all the neighbors;
            # although we will see duplicate neighbors
            for _ in range(len(queue)):
                cell = queue.pop(0)
                row = cell[0]
                col = cell[1]
                neighbors = getNeighbors(row, col)
                for neighbor in neighbors:
                    neighbor_row, neighbor_col = neighbor
                    if (neighbor_row,neighbor_col) in seen or grid[neighbor_row][neighbor_col] == 0:
                        continue
                    seen.add((neighbor_row, neighbor_col))
                    queue.append((neighbor_row,neighbor_col))
                    if grid[neighbor_row][neighbor_col] == 1:
                        num_fresh -= 1
                    # end early
                    if num_fresh == 0:
                        return time
                    grid[neighbor_row][neighbor_col] = 2
        print(num_fresh)
        if num_fresh > 0:
            return -1





                


        