class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        from_left = [0] * n
        from_right = [0] * n

        # essentially you wanna track whatever is highest to your left/right
        # reason being?
        # you track highest of both left/right, then you take the 
        # lower of those 2 for your bounds
        # and then you also just subtract whatever your current height is
        # to get the amount of water trapped (or 0 if it falls below)

        for i in range(1,n):
            from_left[i] = max(from_left[i-1], height[i])

        for i in range(n-2,-1,-1):
            from_right[i] = max(from_right[i+1], height[i])

        total = 0

        for i in range(n):
            total += max(0, min(from_left[i], from_right[i]) - height[i])
        return total