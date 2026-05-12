class KthLargest:
    # so usually you want to use a heap for kth largest elem
    # in this case not sure we c
    # ah so keep a size k min heap

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        # min heap by default
        heapq.heapify(self.nums)
        self.k = k
        while len(self.nums) > k:
            heapq.heappop(self.nums)



    def add(self, val: int) -> int:
        # essentially the root is always the smallest of the big nums
        # and it'll be the kth largest in this case
        # just think about like bubbling down
        # the root is smallest, everything thing else is larger
        # if we used a max heap, the root is the largest
        # and we dont know anything about the other elements
        # so inserting would not make sense
        if not self.nums:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heappop(self.nums)
            heapq.heappush(self.nums, val)
        return self.nums[0]
