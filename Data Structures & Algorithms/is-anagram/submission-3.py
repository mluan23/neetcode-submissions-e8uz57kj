class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # anagram if they have same counts of letters
        counts = [0] * 26

        for c in s:
            counts[ord(c) - ord('a')] += 1
        for c in t:
            counts[ord(c) - ord('a')] -= 1
        for num in counts:
            if num != 0:
                return False
        return True