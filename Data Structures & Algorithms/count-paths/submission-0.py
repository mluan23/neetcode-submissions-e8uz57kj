class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # so the only moves are down and to the right
        # so i think 1 bc base case is 1?
        dp = [[1 for _ in range(n)] for _ in range(m)]
        print(dp)
        for i in range(m):
            for j in range(n):
                # due to up/left borders only hav
                # 1 possible path
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
# what we know is the bordering pieces will always
# only ever be part of one path
# so its a tree; either choose to move right or move down
# base case:
# if just 1 x 1, then 1
# recurrence:
# dp[i][j] = dp[i-1][j]
# dp[i][j] = dp[i][j-1] + 1 if moving right
# 1 x 2 grid:
# 1 path; just move right