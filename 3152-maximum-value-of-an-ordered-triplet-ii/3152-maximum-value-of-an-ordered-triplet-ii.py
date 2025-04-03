class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        highest = 0  # to store highest number till now: nums[i]
        highest_diff = 0  # to store highest diff: nums[i] - nums[j]
        answer = 0  # to store current max value: (nums[i] - nums[j]) * nums[k]
        for num in nums:
            answer = max(answer, highest_diff * num)
            highest_diff = max(highest_diff, highest - num)
            highest = max(highest, num)
        return answer