class Solution:
    def countBits(self, n: int) -> List[int]:
        def countOnes(n):
            c = 0
            for _ in range(32):
                if n & 1:
                    c += 1
                n = n >> 1
            return c
        res = [0] * (n+1)
        for i in range(1,n+1):
            res[i] = countOnes(i)
        return res
        