"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # so the way to do this is with a heap
        # we wanna sort by starting time this time
        # and our heap should be based on the ending time
        # basically if ending time is done then you can remove it
        # and then at the end we just return the length of the heap
        
        # sorts in ascending order of start time
        intervals = sorted(intervals, key=lambda x: x.start)
        # now we a min heap
        # by default it's min heap luckily
        heap = []
        for interval in intervals:
            if not heap:
                heapq.heappush(heap, interval.end)
            else:
                # the heap is already there, check if the cur interval
                # start time is less; if it is, there is conflict
                if interval.start < heap[0]:
                    heapq.heappush(heap, interval.end)
                else:
                    heapq.heappop(heap)
                    heapq.heappush(heap, interval.end)
        return len(heap)
        