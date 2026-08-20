class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # for this, you greedily just keep track of the highest freq
        # character for each substring
        # and then you replace as much as you can 

        left = 0
        right = 0
        longest = 0
        frequencies = dict()
        while right < len(s):
            # check if valid
            c = s[right]
            frequencies[c] = frequencies.get(c,0) + 1
            max_freq = max(frequencies.values())

            # so we have the max freq
            # and the relation is that we have r - l + 1 - max_freq replacements
            # its valid
            if right - left + 1 - max_freq <= k:
                longest = max(longest, right - left + 1)
            else:
                frequencies[s[left]] -= 1
                left += 1
            right += 1

        return longest