from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Initialize the deque and the result list
        dq = deque()
        result = []

        for i in range(len(nums)):
            # Remove indices that are out of the current window
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # Remove indices from the deque whose corresponding values are less than nums[i]
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # Add the current index to the deque
            dq.append(i)

            # If the window has at least k elements, add the maximum to the result
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result
