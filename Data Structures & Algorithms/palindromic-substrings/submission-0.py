class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        # dp[0] = 1
        for i in range(n):
            l, r = i,i
            if i > 0:
                dp[i] = dp[i-1]
            while l >= 0 and r < n and s[l] == s[r]:
                dp[i] += 1
                l -= 1
                r += 1
            l,r = i,i+1
            while l >= 0 and r < n and s[l] == s[r]:
                dp[i] += 1
                l -= 1
                r += 1
        return dp[-1]