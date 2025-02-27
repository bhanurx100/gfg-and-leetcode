from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()  # Sort to handle duplicates easily

        def backtrack(start, target, path):
            if target == 0:  # Found a valid combination
                result.append(path[:])  # Append a copy
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates (only allow the first occurrence in a recursive level)
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # If the current number exceeds the remaining target, stop exploring further
                if candidates[i] > target:
                    break

                # Include the number and move to the next index (each number is used once)
                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i], path)
                path.pop()  # Backtrack

        backtrack(0, target, [])
        return result
