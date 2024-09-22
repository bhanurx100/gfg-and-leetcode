class Solution:
    def binarySearch(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        counter = 0
        for num in nums:
            if self.binarySearch(nums, num + diff) and self.binarySearch(nums, num + 2 * diff):
                counter += 1
        return counter