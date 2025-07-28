class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Step 2: Precompute the maximum OR of all elements
        max_or = 0
        for num in nums:
            max_or |= num
        
        count = 0
        
        # Step 3: Define recursive backtracking function
        def backtrack(index, current_or):
            nonlocal count

            # Step 4: Base case – all elements processed
            if index == len(nums):
                # Step 4: Check if OR equals max OR
                if current_or == max_or:
                    count += 1  # Valid subset found
                return
            
            # Step 5: Recursive calls
        
            # Include current number
            backtrack(index + 1, current_or | nums[index])
        
            # Exclude current number
            backtrack(index + 1, current_or)
        
        # Step 6: Start backtracking from index 0 and OR value 0
        backtrack(0, 0)
        
        # Step 6: Return final count
        return count 