import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # Max Heap (stores the smaller half, as negative numbers)
        self.large = []  # Min Heap (stores the larger half)

    def addNum(self, num: int) -> None:
        # Step 1: Add to max heap (invert to simulate max heap)
        heapq.heappush(self.small, -num)
        
        # Step 2: Balance - move the largest in small to large heap
        heapq.heappush(self.large, -heapq.heappop(self.small))
        
        # Step 3: Ensure small heap has equal or more elements than large
        if len(self.small) < len(self.large):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        # If odd, the median is the top of max heap
        if len(self.small) > len(self.large):
            return -self.small[0]
        # If even, the median is the average of the tops of both heaps
        return (-self.small[0] + self.large[0]) / 2
