class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        if n==1:return nums[0]
        if n==2: return max(nums[0],nums[1])
        def rob_linear(arr:List[int])->int:
            m=len(arr)
            if m==0:return 0
            if m==1: return arr[0]
            prev2=arr[0]
            prev1=max(arr[0],arr[1])
            for i in range(2,m):
                curr=max(prev1,arr[i]+prev2)
                prev2=prev1
                prev1=curr
            return prev1
        case1=rob_linear(nums[:-1])
        case2=rob_linear(nums[1:])
        return max(case1,case2)