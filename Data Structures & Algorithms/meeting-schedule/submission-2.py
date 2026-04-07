"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort intervals in ascending by start
        intervals.sort(key=lambda x: x.start, reverse=False)
        if len(intervals) == 0:
            return True
        start = intervals[0].start
        for i in range(len(intervals) - 1):
            if intervals[i + 1].start < intervals[i].end:
                return False
        return True
