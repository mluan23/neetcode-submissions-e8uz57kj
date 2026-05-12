class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        elem = None
        for i in range(k):
            elem = heapq.heappop(nums)
        return -elem