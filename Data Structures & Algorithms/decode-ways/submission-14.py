class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[-1] = 1
        # handle leading zero case
        for i in range(len(s)-1, -1, -1):
            # need to handle 0, since it 
            # not map to a letter
            # cause its a leadig zero, so 0
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            if i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i+1] in '0123456'):
                dp[i] += dp[i+2] 
        return dp[0]
                
        # so if the prev s[i] makes it correct, then you can add another decode?
        # your choices: 
        # - take the current one (guaranteed +1?)
        # - take the current + next, if <= 26
        # only ever need to look at 2 chars max