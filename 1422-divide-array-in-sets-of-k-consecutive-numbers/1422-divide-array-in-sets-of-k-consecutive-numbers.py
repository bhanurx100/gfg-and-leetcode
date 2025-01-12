class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums)%k!=0:
            return False
        count=Counter(nums)
        min_heap=list(count.keys())
        heapq.heapify(min_heap)
        while min_heap:
            first=min_heap[0]
            for i in range(first,first+k):
                if count[i]==0:
                    return False
                count[i]-=1
                if count[i]==0:
                    if i!=min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
        return True