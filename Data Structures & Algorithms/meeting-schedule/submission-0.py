"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort list by intervals
        if len(intervals) == 0: return True

        intervals = sorted(intervals, key= lambda x:x.start)

        tmp = intervals[0]
        for interval in intervals[1:]:
            if interval.start < tmp.end:
                return False
            tmp = interval
    
        return True