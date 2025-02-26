class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        sum,maxsum,minsum=0,0,0
        for num in nums:
            sum+=num
            minsum=min(minsum,sum)
            maxsum=max(maxsum,sum)
        return abs(maxsum-minsum)
