"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # we keep a heap to track when a room is available
        # sort by start time
        # keep a heap to track 
        # why do we sort by start and not end?
        # sort by starts; just pop off the ends each time, easy enough

        intervals = sorted(intervals, key=lambda x: x.start)
        # use a min heap
        heap = []
        for interval in intervals:
            if heap and heap[0] <= interval.start:
                heapq.heappop(heap)
            heapq.heappush(heap, interval.end)
        return len(heap)
