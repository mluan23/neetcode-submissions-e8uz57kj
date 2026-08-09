class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()

        for word in strs:
            char_counts = [0] * 26
            for c in word:
                char_counts[ord(c) - ord('a')] += 1
            if tuple(char_counts) not in anagrams:
                anagrams[tuple(char_counts)] = [word]
            else:
                anagrams[tuple(char_counts)].append(word)
        return list(anagrams.values())