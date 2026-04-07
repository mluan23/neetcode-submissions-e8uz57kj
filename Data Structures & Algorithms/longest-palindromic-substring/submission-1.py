class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        maxLen = 0
        for i in range(len(s)):
            l, r = i, i
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLen :
                    maxLen = r-l+1
                    # not inclusive
                    res = s[l:r+1]
                l-=1
                r+=1

            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) >maxLen:
                    maxLen = r-l+1
                    res = s[l:r+1]
                l-=1
                r+=1
        return res



# so base case, for 1, we always know it'll be itself
# so worst scenario, it'll be a 1 letter palindrome
# if we add another one we have to do a palindrome check
# so we know palindrome works by examining the outer 2
# so we want to start at the ends and move inwards
# so the brute force way is to check if possible substring;
# is that subtstring a palindrome? the issue with this
# is it'll be really slow

# so it turns out start at ctr makes most sense,
# but you gotta treat every char as the ctr