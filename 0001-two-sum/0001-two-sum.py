class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            if target - nums[i] in numMap:
                return [numMap[target - nums[i]], i]
            numMap[nums[i]] = i
        return []
