class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        st=[]
        res=[-1]*n
        for i in range (2*n):
            current_index=i%n
            while st and nums[current_index]>nums[st[-1]]:
                top_index=st.pop()
                res[top_index]=nums[current_index]
            if i<n:
                st.append(current_index)
        return res