"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if len(intervals) == 0: return 0
        if len(intervals) == 1: return 1
        

        intervals.sort(key = lambda x: x.start)
        start = [interval.start for interval in intervals]
        end = sorted([interval.end for interval in intervals])

        l, r, rooms, maxrooms = 0, 0, 0, 0

        while l < len(start):
            # a new meeting starts:
            if start[l] < end[r]:
                l = l+1
                rooms += 1
                maxrooms = max(maxrooms, rooms)
            # a meeting ends >= start
            else:
                r += 1
                rooms -= 1
        
        return maxrooms