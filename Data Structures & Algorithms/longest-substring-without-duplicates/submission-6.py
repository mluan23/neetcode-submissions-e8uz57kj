class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum = 0
        seen = set()
        left = 0
        right = 0
        while right < len(s):
            if s[right] not in seen:
                maximum = max(right-left + 1, maximum)
                seen.add(s[right])
                right += 1
            else:
                seen.remove(s[left])
                left += 1
        return maximum
