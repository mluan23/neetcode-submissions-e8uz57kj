class Solution:

    def encode(self, strs: List[str]) -> str:
        # pretty much you encode with break char, then num chars to expect
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        idx = 0
        while idx < len(s):
            num = ""
            # first get the number
            while s[idx] != "#":
                num += s[idx]
                idx += 1
            # trim the pound sign
            idx += 1
            # now get the word?
            num = int(num)
            res.append(s[idx:idx+num])
            # print(num)
            # print(s[idx:num])
            idx += num
        return res
