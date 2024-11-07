class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # Initialize a stack to keep track of indices of elements we haven't found a next greater element for
        stack = []
        
        # Initialize the result list to contain all -1s (assuming we won't find any next greater element)
        result = [-1] * len(nums)
        
        # Loop through the array twice (to handle circularity) and process each element
        for _ in range(2):
            for i in range(len(nums)):
                # Pop elements off the stack if they are less than the current element and update their result
                while stack and nums[stack[-1]] < nums[i]:
                    result[stack.pop()] = nums[i]
                
                # Add the current index to the stack
                stack.append(i)
        
        # Return the result list
        return result