class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1 
        right = max(piles)

        while left <= right:
            eating_speed = (left + right) // 2
            num_hours = 0
            for pile in piles:
                num_hours += math.ceil(pile / eating_speed) + 1
            # means you can decrease eating rate
            if num_hours <= h:
                right = eating_speed - 1
            else:
                left = eating_speed + 1
        return right