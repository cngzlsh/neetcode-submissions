class MedianFinder:
    import heapq
    def __init__(self):
        self.n = 0
        self.maxH = [] # for smaller half
        self.minH = [] # for larger half

        heapq.heapify(self.maxH)
        heapq.heapify(self.minH)
        

    def addNum(self, num: int) -> None:
        if self.n == 0:
            heapq.heappush(self.maxH, -num)
            self.n += 1
            return
        # ensure lower half is always same or greater than upper half
        # if currently balanced
        if self.n % 2 == 0:
            if num <= -self.maxH[0]:
                heapq.heappush(self.maxH, -num)
            else:
                heapq.heappush(self.minH, num)
                num2 = heapq.heappop(self.minH) 
                heapq.heappush(self.maxH, -num2)
        # if currently imbalanced
        else:
            if num <= -self.maxH[0]:
                heapq.heappush(self.maxH, -num)
                num2 = heapq.heappop(self.maxH)
                heapq.heappush(self.minH, -num2)
            else:
                heapq.heappush(self.minH, num)
        self.n += 1
        
        
    def findMedian(self) -> float:
        if self.n % 2 == 0:
            return (-self.maxH[0] + self.minH[0]) / 2
        else:
            return (-self.maxH[0])
        
        