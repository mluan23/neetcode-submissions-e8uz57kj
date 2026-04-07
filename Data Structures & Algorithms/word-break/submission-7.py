class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # first of all, is there a brute force way to do this?
        # 
        start_idx = 0
        # whats dp[i] gonna be?
        # can the given string be split here?
        # maybe thats what dp[i] will be, 
        # and then gotta do a backtrack?
        # so every char do what?
        dp = [False] * (len(s)+1)
        dp[-1] = True
        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                cur_str = s[i : i + len(word)]
                print(cur_str)
                if cur_str == word:
                    dp[i] = dp[i + len(word)] or dp[i]
        return dp[0]

# perhaps track shortest/longest for a given?

# cant just immediately remove word upon seeing it, 
# due to word overlaps
# so idea should, as you go through each char of the sting,
# can you split this substring?