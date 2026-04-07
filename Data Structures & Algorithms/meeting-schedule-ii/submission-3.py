"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # hmm so hows this different
        # well whats important in this q
        # so essentially the number of overlaps
        # is the number of meeting rooms we need
        # so how do we count the number of overlaps?
        # if we sort by endings, cant we just go backwards?
        # thought we need to track both start and end, to see the range
        # ohhh
        # push a start node in
        # keep going till we find its end?
        # then we can kinda see everyone who has merged into there
        # essentially we can just merge everyone into one interval
        
        # so, sort everything by start time
        # record the current start time, and the current end time
        # any time you get a conflict pop off your cur start and omve to the next one
        intervals.sort(key=lambda x: x.start)
        min_heap = []

        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)
        return len(min_heap)

