class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k==0 or n>=k+maxPts-1: return 1.0
        dp=[0.0]*(n+1)
        dp[0]=1
        wsum, prob, l=1.0, 0.0, 0
        for r in range(1, n+1):
            dp[r]=wsum/maxPts
            if r<k:
                wsum+=dp[r]
            else:
                prob+=dp[r]
            if r>=maxPts:
                wsum-=dp[l]
                l+=1
        return prob 
        