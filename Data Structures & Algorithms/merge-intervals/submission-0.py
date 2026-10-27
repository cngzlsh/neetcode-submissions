class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1: return intervals

        intervals.sort(key = lambda x: x[0])
        
        curr_interval = intervals[0]
        res = [curr_interval]
        for next_interval in intervals[1:]:
            if curr_interval[0] <= next_interval[0] <= curr_interval[1]:
                merged = [min(curr_interval[0], next_interval[0]), max(curr_interval[1], next_interval[1])]
                res.pop()
                res.append(merged)
                curr_interval = merged
            else:
                res.append(next_interval)
                curr_interval = next_interval
        
        return res
