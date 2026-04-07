class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n-1
        maximum = 0
        while left < right:
            left_height = heights[left]
            right_height = heights[right]
            maximum = max(min(left_height, right_height) * (right-left), maximum)
            print(maximum)

            if left_height < right_height:
                left += 1
            else:
                right -= 1
        return maximum


        