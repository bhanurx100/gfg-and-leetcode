from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Pair each number with its index
        indexed_nums = [(num, i) for i, num in enumerate(nums)]

        # Step 2: Sort by number value (descending), so bigger numbers come first
        indexed_nums.sort(key=lambda x: -x[0])

        # Step 3: Take top k elements (best k values)
        top_k = indexed_nums[:k]

        # Step 4: Sort by original index to preserve order
        top_k.sort(key=lambda x: x[1])

        # Step 5: Return only the values
        return [num for num, i in top_k]
