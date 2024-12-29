class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Step 1: Preprocess nums2 to find next greater elements
        next_greater = {}
        stack = []
        
        for num in nums2:
            # Maintain a decreasing stack; update next_greater when a greater element is found
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)
        
        # Remaining elements in the stack don't have a next greater element
        while stack:
            next_greater[stack.pop()] = -1
        
        # Step 2: Map results for nums1 using the preprocessed data
        return [next_greater[num] for num in nums1]
