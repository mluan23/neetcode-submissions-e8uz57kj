class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams=  dict()

        for s in strs:
            counts = [0] * 26
            for i in range(len(s)):
                c = s[i]

                counts[ord(c) - ord('a')] += 1

            if tuple(counts) in anagrams:
                anagrams.get(tuple(counts)).append(s)
            else:
                anagrams[tuple(counts)] = [s]
        return list(anagrams.values())