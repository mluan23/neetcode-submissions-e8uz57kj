"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    import heapq
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # so for this, we sort by the starting times
        # then we iterate through them
        # if the current staritng time is larger than the 
        # earliest ending time, we need a new room
        # therefore add this interval to the heap as well
        # else we'll just pop off the previous and place the new
        # one on
        # then we return the len of the heap
        min_heap = []
        # heapq.heapify(min_heap)

        for interval in intervals:
            # do i need to make a new room?
            # is the next room available?
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)
            
        return len(min_heap)