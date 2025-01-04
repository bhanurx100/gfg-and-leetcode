class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        for i in range(1<<n):
            subset=[]
            for j in range(n):
                if i &(1<<j):
                    subset.append(nums[j])
            res.append(subset)
        return res