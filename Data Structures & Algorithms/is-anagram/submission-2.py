class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = [0] * 26

        for i in range(len(s)):
            c = s[i]
            char_count[ord(c) - ord('a')] += 1

        for i in range(len(t)):
            c = t[i]
            char_count[ord(c) - ord('a')] -= 1
        for i in range(26):
            if char_count[i] != 0:
                return False
        return True