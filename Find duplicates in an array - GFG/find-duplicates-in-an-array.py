class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	d=dict()
    	s=set()
    	for i in arr:
    	    if i not in d.keys():
    	        d[i]=1
    	    else:
    	        s.add(i)
    	if(len(s)==0):
    	    return [-1]
    	s=list(s)
    	s.sort()
    	return s
    	
    	    


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends