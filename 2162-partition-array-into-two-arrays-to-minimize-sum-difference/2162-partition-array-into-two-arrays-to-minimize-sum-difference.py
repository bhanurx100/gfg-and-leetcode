import collections
import math
from bisect import bisect_left
from typing import List

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2
        total_sum = sum(nums)
        min_diff = float('inf')

        left_half = nums[:n]
        right_half = nums[n:]

        def generate_sums(arr: List[int]) -> collections.defaultdict:
            sums_by_k = collections.defaultdict(list)
            num_elements = len(arr)

            for i in range(1 << num_elements):
                current_sum = 0
                count = 0
                for j in range(num_elements):
                    if (i >> j) & 1:
                        current_sum += arr[j]
                        count += 1
                sums_by_k[count].append(current_sum)
            return sums_by_k

        left_sums = generate_sums(left_half)
        right_sums = generate_sums(right_half)

        for k in left_sums:
            left_sums[k].sort()
        for k in right_sums:
            right_sums[k].sort()

        for i in range(n + 1):
            j = n - i

            if i not in left_sums or j not in right_sums:
                continue

            current_left_sums = left_sums[i]
            current_right_sums = right_sums[j]

            for s1 in current_left_sums:
                target_s2 = (total_sum / 2) - s1

                idx = bisect_left(current_right_sums, target_s2)

                if idx < len(current_right_sums):
                    s2 = current_right_sums[idx]
                    current_partition_sum = s1 + s2
                    min_diff = min(min_diff, abs(2 * current_partition_sum - total_sum))

                if idx > 0:
                    s2 = current_right_sums[idx - 1]
                    current_partition_sum = s1 + s2
                    min_diff = min(min_diff, abs(2 * current_partition_sum - total_sum))

        return min_diff
