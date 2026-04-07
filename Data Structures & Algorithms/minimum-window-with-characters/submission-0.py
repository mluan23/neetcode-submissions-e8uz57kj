class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # checking if a substring contains 
        # the given chars
        res = ""
        cur_string = ""
        res_len = sys.maxsize
        counts = {}

        # tracks the t
        for i in t:
            counts[i] = 1 + counts.get(i, 0)

        l, r = 0, 0
        while r < len(s):
            # this should mean the string is not yet valid
            if max(counts.values()) > 0:
                cur_string += s[r]
                print(s[r])
                print(counts)
                if s[r] in counts:
                    counts[s[r]] = counts.get(s[r]) - 1
                print(counts)
                r += 1
        

            # this should mean the string is valid
            if max(counts.values()) < 1:
                print('made it')
                while max(counts.values()) < 1:
                    if len(cur_string) <= res_len:
                        res_len = len(cur_string)
                        res = cur_string
                    if (s[l] in counts):
                        counts[s[l]] += 1
                    l += 1
                    cur_string = cur_string[1:]
                    print(cur_string)
                    print(counts)
            print(cur_string)

        return res