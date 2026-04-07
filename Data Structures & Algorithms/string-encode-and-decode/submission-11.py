class Solution:

    def encode(self, strs: List[str]) -> str:
        # keep track of string length
        res = ''
        for i in strs:
            res += str(len(i))
            res += '|'
            res += i
        return res


    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        i = 0
        count = ''
        if len(s) == 0:
            return []
        if len(s) == 2:
            return [""]
        while s[i] != '|':
            count += s[i]
            i += 1
        count = int(count)
        i += 1
        while i < len(s):
            cur = ''
            for j in range(count):
                cur += s[i]
                i += 1
            res.append(cur)
            cur = ''
            count = ''
            if i == len(s):
                break
            while s[i] != '|':
                count += s[i]
                i+= 1
            count = int(count)
            i += 1
        return res


