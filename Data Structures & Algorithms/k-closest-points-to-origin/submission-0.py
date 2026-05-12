class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # closest = smallest distance
        # can either use a min heap
        # add every elem to min heap
        # then pop off k elements
        # or we can use a max heap
        # make it size k
        # if the next distance is less, then 
        # pop off current max
        # push on new elem
        # lets try the max heap method, as i did min heap one b4
        max_heap = []
        for x1, y1 in points:
            distance = -math.sqrt((x1)**2 + (y1)**2)
            if len(max_heap) < k:
                heapq.heappush(max_heap, (distance, [x1, y1]))
            else:
                # we want > b/c it is max_heap, uses negatives
                if distance > max_heap[0][0]:
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, (distance, [x1, y1]))
        res = []
        for i in range(len(max_heap)):
            res.append(max_heap[i][1])
        return res


                