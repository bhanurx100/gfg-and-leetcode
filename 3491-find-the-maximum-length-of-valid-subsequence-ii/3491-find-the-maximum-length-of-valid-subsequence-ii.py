class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        max_length = 0
        
        for target_rem in range(k):
            # last[r] = length of longest subsequence ending with remainder r
            last = [0] * k
            
            for num in nums:
                curr_rem = num % k
                # To get target_rem, previous number needs remainder:
                need_rem = (target_rem - curr_rem) % k
                
                # We can extend the subsequence ending at need_rem
                last[curr_rem] = last[need_rem] + 1
            
            max_length = max(max_length, max(last))
        
        return max_length