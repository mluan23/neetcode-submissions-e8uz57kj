class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        seen = set()
        left = 0
        right = 0

        while right < len(s):
            while s[right] in seen:
                # this means it is not a valid substring
                seen.remove(s[left])
                left += 1
            
            longest = max(longest, right - left + 1)
            seen.add(s[right])
            right += 1
        return longest