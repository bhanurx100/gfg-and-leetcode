class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i]*= 2
                nums[i + 1] = 0   # <-- performing the "operation."  
      
        nums.sort(key=lambda x: x == 0)   # Sorting on a boolean key: False, then True
        
        return nums 