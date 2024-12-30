class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n=len(nums)
        min_stack=[]
        min_sum=0
        for i in range(n+1):
            while min_stack and nums[min_stack[-1]]>(nums[i] if i<n else -float('Inf')):
                j=min_stack.pop()
                k=min_stack[-1] if min_stack else -1
                min_sum+=(j-k)*(i-j)*nums[j]
            min_stack.append(i)
        max_stack=[]
        max_sum=0
        for i in range(n+1):
            while max_stack and nums[max_stack[-1]]<(nums[i] if i<n else float('Inf')):
                j=max_stack.pop()
                k=max_stack[-1] if max_stack else -1
                max_sum+=(j-k)*(i-j)*nums[j]
            max_stack.append(i)
        ans=max_sum-min_sum
        return ans