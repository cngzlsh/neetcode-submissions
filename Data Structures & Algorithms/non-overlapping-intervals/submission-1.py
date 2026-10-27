class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by first key
        # whenever an overlap, abandon the one that finishes later
        

        if len(intervals) == 1: return 0

        intervals.sort(key = lambda x: x[0])

        res = 0
        curr_interval = intervals[0]
        for i, next_interval in enumerate(intervals[1:]):
            if curr_interval[0] <= next_interval[0] < curr_interval[1]:
                res += 1

                # if curr_interval finishes later, abandon it and replace with new interval
                if curr_interval[1] >= next_interval[1]:
                    curr_interval = next_interval
                
                # else, abandon the new interval
                else:
                    continue
            
            else:
                curr_interval = next_interval
        
        return res
