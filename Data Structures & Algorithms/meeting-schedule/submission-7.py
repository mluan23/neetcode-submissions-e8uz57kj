"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # if the start time of one interval lies in between
        # the start and end time of another interval:
        # then there is a conflict and so false
        # so the way we check this is 
        # sort by ending times
        if not intervals:
            return True
        intervals = sorted(intervals, key=lambda x: x.end)

        prev = intervals[0]

        for i in range(1,len(intervals)):
            if intervals[i].start < prev.end:
                return False
            prev = intervals[i]
        return True
        