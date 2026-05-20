class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequencies = {}

        left = 0
        right = 0
        longest = 0
        while right < len(s):
            # find the one with the highest frequency
            # thats the one we want to keep
            # and then you replace the rest essentially
            left_char = s[left]
            right_char = s[right]
            frequencies[right_char] = frequencies.get(right_char, 0)+1
            # the amount to KEEP in the window
            highest_freq = max(frequencies.values())
            # is this a valid substring? 
            # the rhs is essentially the number of chars we replace
            if highest_freq >= right - left + 1 - k:
                longest = max(longest, right-left + 1)
                right += 1
            else:
                left += 1
                frequencies[left_char] = frequencies.get(left_char)-1
            # right += 1
        return longest
