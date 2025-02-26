from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []  # Stores all valid combinations

        def backtrack(start, target, path):
            # Base case: if target becomes zero, we found a valid combination
            if target == 0:
                result.append(path[:])  # Append a copy of path to result
                return

            # Iterate through candidates starting from 'start' index to avoid duplicates
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue  # Skip if the number is greater than the remaining target

                # Include the candidate and explore further (same index allows reuse)
                path.append(candidates[i])
                backtrack(i, target - candidates[i], path)
                path.pop()  # Backtrack and remove the last added number

        # Start backtracking from index 0 with the full target
        backtrack(0, target, [])
        return result
