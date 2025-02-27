from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()  # Sort to handle duplicates easily
        
        def backtrack(start, path):
            result.append(path[:])  # Store current subset
            
            for i in range(start, len(nums)):
                # Skip duplicate elements
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                # Include nums[i] and recurse
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()  # Backtrack to previous state
        
        backtrack(0, [])
        return result
