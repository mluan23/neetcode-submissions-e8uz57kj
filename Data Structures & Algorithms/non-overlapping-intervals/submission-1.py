class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[0])
        # print(intervals)
        prev = intervals[0]
        count = 0
        for i in range(1, len(intervals)):
            cur = intervals[i]
            # print(prev)

            # means overlapping so need to remove the one w 
            # later ending time
            if prev[1] > cur[0]:
                if prev[1] > cur[1]:
                    prev = cur
                count +=1
            else:
                prev = cur
        return count
            



