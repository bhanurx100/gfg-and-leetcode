#from collections import counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        count=Counter(hand)
        min_heap=list(count.keys())
        heapq.heapify(min_heap)
        while min_heap:
            first=min_heap[0]
            for i in range(first,first+groupSize):
                if count[i]==0:
                    return False
                count[i]-=1
                if count[i]==0:
                    if i!=min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
        return True
