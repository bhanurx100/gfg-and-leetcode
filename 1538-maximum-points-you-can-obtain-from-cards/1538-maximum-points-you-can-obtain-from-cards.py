class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        total_sum=sum(cardPoints)
        if k==n:
            return total_sum
        window_size=n-k
        curr_window_sum=sum(cardPoints[:window_size])
        min_window_sum=curr_window_sum
        for i in range(window_size,n):
            curr_window_sum+=cardPoints[i]-cardPoints[i-window_size]
            min_window_sum=min(min_window_sum,curr_window_sum)
        return total_sum-min_window_sum
