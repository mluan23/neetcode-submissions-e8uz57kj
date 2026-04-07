class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maximum = 0
        left = 0
        right = 0

        char_counts = dict()

        while right < len(s):
            r = s[right]
            char_counts[r] = char_counts.get(r,0) + 1
            max_char = max(char_counts.values())

            # invalid replacements
            if right - left + 1 - max_char > k:
                l = s[left]
                char_counts[l] -= 1
                left += 1
            # valid replacements
            maximum = max(maximum, right - left + 1)
            right += 1
        return maximum

        # maximum = 0
        # [A A A B A B B], k = 1
        #      L   R 
        # 