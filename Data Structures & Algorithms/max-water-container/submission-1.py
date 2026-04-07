class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        left = 0
        right = 0

        # brute force is to calc the dist between all
        
        for i in range(len(heights)):
            for j in range(len(heights)):
                maximum = max(min(heights[i], heights[j]) * abs(i-j), maximum)
        return maximum 
