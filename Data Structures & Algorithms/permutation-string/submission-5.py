class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # ok so how do you get permutations?
        # ok so its not based on character counts
        # its based on what then?
        # we know that we only should ever compare shortest string against longest
        # oh its just sliding window with character counts
        # ok so s1 should always be shorter than s2 given the constraints
        # yeah ok so not any substring of s1, strictly s1, makes it easy then
        if len(s1) > len(s2):
            return False
        # we should use arrays to have easier equality check
        counts1 = [0] * 26
        counts2 = [0] * 26
        left = 0
        right = len(s1) - 1
        for i in range(right+1):
            counts1[ord(s1[i]) - ord('a')] += 1
            counts2[ord(s2[i])- ord('a')] += 1
        right += 1
        while right < len(s2):
            if counts1 == counts2:
                # print(counts1, counts2)
                return True
            counts2[ord(s2[left])- ord('a')] -= 1
            counts2[ord(s2[right])- ord('a')] += 1

            left+=1 
            right+=1
        return False
        

