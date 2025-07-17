from typing import List
from collections import defaultdict
from itertools import combinations
import bisect

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2
        total_sum = sum(nums)
        left, right = nums[:n], nums[n:]

        def get_subset_sums(arr):
            subset_sums = defaultdict(list)
            length = len(arr)
            for k in range(length + 1):
                for comb in combinations(arr, k):
                    subset_sums[k].append(sum(comb))
            return subset_sums

        left_sums = get_subset_sums(left)
        right_sums = get_subset_sums(right)

        min_diff = float('inf')
        for l_count in range(n + 1):
            r_count = n - l_count
            left_list = left_sums[l_count]
            right_list = sorted(right_sums[r_count])

            for s1 in left_list:
                # Target sum1: we try to approach total_sum / 2
                target = total_sum // 2
                target_s2 = target - s1

                idx = bisect.bisect_left(right_list, target_s2)
                for i in [idx - 1, idx]:
                    if 0 <= i < len(right_list):
                        s2 = right_list[i]
                        sum1 = s1 + s2
                        sum2 = total_sum - sum1
                        diff = abs(sum1 - sum2)
                        min_diff = min(min_diff, diff)

        return min_diff
