import heapq

class Solution:
    def minimumDifference(self, A):
        n = len(A) // 3
        lenA = len(A)

        # Step 1: Prefix - Max heap (simulate with negative numbers)
        max_heap = []
        left = [0] * lenA
        sum_left = 0

        # Step 2: Build left[] where left[i] is min sum of n elements from 0 to i
        for i in range(lenA):
            heapq.heappush(max_heap, -A[i])  # Use negative to simulate max heap
            sum_left += A[i]
            if len(max_heap) > n:
                sum_left += heapq.heappop(max_heap)  # Remember this is negative
            if i >= n - 1:
                left[i] = sum_left

        # Step 3: Suffix - Min heap for largest n elements from right side
        min_heap = []
        right = [0] * (lenA + 1)
        sum_right = 0

        # Step 4: Build right[] where right[i] is max sum of n elements from i to end
        for i in range(lenA - 1, -1, -1):
            heapq.heappush(min_heap, A[i])
            sum_right += A[i]
            if len(min_heap) > n:
                sum_right -= heapq.heappop(min_heap)
            if i <= lenA - n:
                right[i] = sum_right

        # Step 5: Find minimum difference between left and right parts
        ans = float('inf')
        for i in range(n - 1, 2 * n):
            ans = min(ans, left[i] - right[i + 1])

        return ans