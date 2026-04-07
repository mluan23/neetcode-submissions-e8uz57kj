class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # so the idea is is you in top right corner,
        # then everyything to left is less, everuthing
        # below is greater (you can reverse theese)
        # cond if you start at the bot left corner
        # if you get to prev
        # think need to keep seen to prevent backtracking
        m = len(matrix)
        n = len(matrix[0])

        # track (i, j)
        seen = set() 

        i = 0
        j = n-1
        while True:
            if (i,j) in seen or i == m or j == -1:
                return False
            seen.add((i,j))
            num = matrix[i][j]
            if num == target:
                return True
            if num < target:
                i += 1
            if num > target:
                j -= 1
        return False
