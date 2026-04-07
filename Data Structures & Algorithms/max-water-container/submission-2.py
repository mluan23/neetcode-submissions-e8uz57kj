class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        left = 0
        right = len(heights)-1

        # brute force is to calc the dist between all
        
        while left < right:
            area = min(heights[left], heights[right]) * abs(left-right)
            maximum = max(area, maximum)
            if heights[left] >= heights[right]:
                right -= 1
            else:
                left += 1
        return maximum

        # like this does work
        # for i in range(len(heights)):
        #     for j in range(len(heights)):
        #         maximum = max(min(heights[i], heights[j]) * abs(i-j), maximum)
        # return maximum 
