class Solution:
    def trap(self, height: List[int]) -> int:
        # prob start at the middle and move outwards ; NOPE YOU SO WRONG BUD
        n = len(height)

        # so this the actual brute force that works. cause the limiting
        # factor is just the shorter of the tallest to left/right bars
        # it slow cause we gotta recalc all these.
        s = 0
        for i in range(n):
            left = max(height[:i+1])
            right = max(height[i:])

            s += min(left, right) - height[i]
        return s

        # so we need at least 3 elevations to trap anything
        # given a position, find the elements to its and left and right
        # that are higher than it, look at min height, and get distance
        # to find area there

        # one fat failure of an attempt

        # for i in range(n):
        #     left = i
        #     right = i+1
        #     area = 0
        #     while left >= 0 and right < n and area <1:
        #         area = max(min(height[left], height[right]) - height[i], area)
        #         if height[left] <= height[i]:
        #             left -= 1
        #         elif height[right] < height[i]:
        #             right +=1
        #     res[i] = area
        # return sum(res)