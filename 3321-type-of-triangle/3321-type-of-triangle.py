class Solution:
    def triangleType(self, nums):
        if not self._is_triangle(nums):
            return "none"
        if self.is_equilateral(nums):
            return "equilateral"
        if self.is_isosceles(nums):
            return "isosceles"
        return "scalene"

    def _is_triangle(self, nums):
        return (nums[0] + nums[1] > nums[2] and
                nums[0] + nums[2] > nums[1] and
                nums[1] + nums[2] > nums[0])

    def is_equilateral(self, nums):
        return nums[0] == nums[1] == nums[2]

    def is_isosceles(self, nums):
        return nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]