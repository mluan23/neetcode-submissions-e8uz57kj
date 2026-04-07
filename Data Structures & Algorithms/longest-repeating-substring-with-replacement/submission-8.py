class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_len = 0
        res = 0
        l, r = 0, 0
        frequencies = [0] * 26
        while l <= r and r < len(s):
            window_len = r - l + 1
            frequencies[ord(s[r]) - ord('A')] += 1
            r += 1
            if not window_len - max(frequencies) <= k:
                frequencies[ord(s[l]) - ord('A')] -= 1
                l += 1
            else:
                res = max(res, window_len)
        return res



# AAAAAABB
# ABABABABABACCCC

# honestly some weird ass sliding window, that is tough to see
# since you want to hold the conditoin windowLen - count(highestElem) <= k