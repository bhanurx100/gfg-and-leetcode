class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(index,curr):
            if index==len(nums):
                result.append(curr[:])
                return
            helper(index+1,curr)
            curr.append(nums[index])
            helper(index+1,curr)
            curr.pop()
        result=[]
        helper(0,[])
        return result