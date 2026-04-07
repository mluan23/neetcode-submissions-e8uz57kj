"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        # one of these intervals problems
        # so there is a conflict if ttwo overlap
        # how to find overlap?
        # if the end of one is later than the start of another
        # then there is a conflict
        # so what you wanna do is sort by ending times
        # and just check the intervals 1 by 1
        # so sort by ascending interval ending time
        intervals.sort(key=lambda x : x.end)

        for i in range(1,len(intervals)):
            prev_end = intervals[i-1].end
            cur_start = intervals[i].start
            if prev_end > cur_start:
                return False
        return True
        
