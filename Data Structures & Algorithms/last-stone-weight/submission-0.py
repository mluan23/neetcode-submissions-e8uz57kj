class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # smallest 
        stones = [-stone for stone in stones]
        heapq.heapify(stones) # makes min heap

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if first != second:
                heapq.heappush(stones,first-second)
            
        return 0 if len(stones) == 0 else -stones[0]
