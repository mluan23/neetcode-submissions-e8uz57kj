class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        right = 0
        maximum = 0
        chars = set()
        while right < n:
            next_char = s[right]
            if next_char in chars:
                chars.remove(s[left])
                left += 1
            else:
                chars.add(next_char)
                right += 1
            maximum = max(len(chars), maximum)

        return maximum
