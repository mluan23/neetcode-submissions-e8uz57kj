class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # so naive just O(n^2) iter thru it all,
        # compare each element to every other element
        # ok so how ca we make tha tafaster?
        # we can instead 
        # so we know the last one will always be 0
        res = [0] * len(temperatures)
        stack = []
        idx = 0
        

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res
            
        

