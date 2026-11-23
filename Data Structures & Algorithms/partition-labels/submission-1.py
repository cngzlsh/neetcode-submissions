class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i, ch in enumerate(s):
            if ch in d:
                d[ch][1] = i
            else:
                d[ch] = [i, i]
        
        # we now have a dictionary of characters with [start, end]
        # now merge intervals
        all_intervals = list(d.values())
        curr_start, curr_end = all_intervals[0]
        merged = []
        for s, e in all_intervals[1:]:
            if s > curr_end:
                merged.append([curr_start, curr_end])
                curr_start, curr_end = s, e

            elif s > curr_start and s < curr_end:
                if e <= curr_end:
                    continue
                else:
                    curr_end = e
        
        merged.append([curr_start, curr_end])
        res = [e-s+1 for s,e in merged]
    
        return res

