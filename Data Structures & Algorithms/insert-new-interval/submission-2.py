class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        inserted = False
        for interval in intervals:
            # entirely before
            if interval[1] < newInterval[0]:
                res.append(interval)
            
            # entirely after
            elif interval[0] > newInterval[1]:
                if not inserted:
                    res.append(newInterval)             
                    inserted = True
                res.append(interval)
            
            else:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
        
        if not inserted:
            res.append(newInterval)
        return res