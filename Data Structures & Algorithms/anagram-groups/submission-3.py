class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 26 ltrs
        counts = [0] * 26
        frequencies = dict()

        for s in strs:
            for letter in s:
                counts[ord(letter) - ord('a')] += 1
            if tuple(counts) in frequencies:
                frequencies[tuple(counts)].append(s)
            else:
                frequencies[tuple(counts)] = [s]
            counts = [0] * 26
        return list(frequencies.values())
