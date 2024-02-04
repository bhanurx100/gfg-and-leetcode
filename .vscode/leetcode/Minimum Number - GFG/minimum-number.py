#User function Template for python3

class Solution:
    def minimumNumber(self, n, arr):
        #code here
        m = z=min(arr)
        for i in arr:
            if i%z<m and i%z!=0:
                m=i%z
        return m        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n=int(input())
        arr=[int(i) for i in input().split()]
        obj=Solution()
        print(obj.minimumNumber(n,arr))
# } Driver Code Ends