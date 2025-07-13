class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum=sum(nums)
        if total_sum%2!=0:
            return False
        target=total_sum//2
        n=len(nums)
        dp=[False]*(target+1)
        dp[0]=True
        for num in nums:
            for t in range(target,num-1,-1):
                if dp[t-num]:
                    dp[t]=True
        return dp[target]