"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        # # two pointers
        # if len(intervals) == 0: return 0
        # if len(intervals) == 1: return 1
        

        # intervals.sort(key = lambda x: x.start)
        # start = [interval.start for interval in intervals]
        # end = sorted([interval.end for interval in intervals])

        # l, r, rooms, maxrooms = 0, 0, 0, 0

        # while l < len(start):
        #     # a new meeting starts:
        #     if start[l] < end[r]:
        #         l = l+1
        #         rooms += 1
        #         maxrooms = max(maxrooms, rooms)
        #     # a meeting ends >= start
        #     else:
        #         r += 1
        #         rooms -= 1
        
        # return maxrooms

        # heap
        import heapq

        intervals.sort(key=lambda x: x.start)
        heap = []              # end times of meetings in progress
        rooms = maxrooms = 0
        for iv in intervals:
            while heap and heap[0] <= iv.start:   # free every room that has ended
                heapq.heappop(heap)
                rooms -= 1
            heapq.heappush(heap, iv.end)          # this meeting takes a room
            rooms += 1
            maxrooms = max(maxrooms, rooms)
        return maxrooms