class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        left = 0
        right = len(s1)
        
        s1_counts = [0] * 26

        s2_counts = [0] * 26

        for i in range(len(s1)):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            s2_counts[ord(s2[i]) - ord('a')] += 1
        if s1_counts == s2_counts:
                return True
        # print("a")

        while right < len(s2):
            # print(s1_counts)
            # print(s2_counts)
            if s1_counts == s2_counts:
                return True
            s2_counts[ord(s2[left]) - ord('a')] -= 1
            left += 1
            s2_counts[ord(s2[right]) - ord('a')] += 1
            right += 1
        if s1_counts == s2_counts:
                return True
        return False



