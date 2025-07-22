class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen =set()
        left=0
        curr_sum=0
        total=0
        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                curr_sum-=nums[left]
                left+=1
            seen.add(nums[right])
            curr_sum+=nums[right]
            total=max(total,curr_sum)
        return total