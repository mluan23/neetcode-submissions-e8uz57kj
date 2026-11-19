class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = [0] * 26
        for c in s:
            counts[ord(c) - ord('a')] += 1
        for c in t:
            counts[ord(c) - ord('a')] -= 1
        return max(counts) == 0 and min(counts) == 0