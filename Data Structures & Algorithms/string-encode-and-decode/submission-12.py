class Solution:

    def encode(self, strs: List[str]) -> str:
        # make the x chars the number of chars to read, and 
        # delimit that guy with a special character
        res = ""
        for s in strs:
            n = len(s)
            res += str(n)
            res += "|"
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        # first_len = int(s[0:s.find("|")+1])
        i = 0
        res = []
        while i < len(s):
            length = ""
            while s[i] != "|":
                length += s[i]
                i += 1
            length = int(length)
            i += 1 # trim the delimiter
            ss = ""
            j = 0
            while j < length:
                ss += s[i+j]
                j += 1
            i += j
            res.append(ss)
        return res
            

        
        
