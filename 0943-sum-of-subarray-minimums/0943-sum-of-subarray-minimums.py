class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        st=[]
        res=[0]*len(arr)
        for i in range(len(arr)):
            while st and arr[st[-1]]>arr[i]:
                st.pop()
            j=st[-1] if st else -1
            res[i]=res[j]+(i-j)*arr[i]
            st.append(i)
        return sum(res)%(10**9+7)