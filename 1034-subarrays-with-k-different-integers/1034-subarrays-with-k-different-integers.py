class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(nums, k):
            count = {}
            left = 0
            result = 0
            
            for right in range(len(nums)):
                if nums[right] not in count:
                    count[nums[right]] = 0
                count[nums[right]] += 1

                while len(count) > k:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        del count[nums[left]]
                    left += 1
                
                result += (right - left + 1)
            
            return result
        
        return atMostK(nums, k) - atMostK(nums, k - 1)
