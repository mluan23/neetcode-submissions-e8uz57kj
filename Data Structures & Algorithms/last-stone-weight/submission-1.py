class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 
        stones = [-n for n in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first_heavy = heapq.heappop(stones)
            second_heavy = heapq.heappop(stones)
            # because max heap
            if first_heavy < second_heavy:
                # second heavy is destroyed
                new_stone = first_heavy - second_heavy
                heapq.heappush(stones, new_stone)
        return -stones[0] if stones else 0