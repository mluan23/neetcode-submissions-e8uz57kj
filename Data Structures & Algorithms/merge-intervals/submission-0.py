class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # how do we sort by?
        # i mean typically when we talk overlappig intervals
        # we talk about sorting by ending time
        # in this case does it make more sense 
        # to start by starting time?
        intervals = sorted(intervals, key=lambda x: x[0])
        merged = [intervals[0]]
        for i in range(1,len(intervals)):
            last = merged[-1]
            # overlap
            if intervals[i][0] <= last[1]:
                merged[-1][1] = max(intervals[i][1], last[1])
            else:
                merged.append(intervals[i])


        return merged
