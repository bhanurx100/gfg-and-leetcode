class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor=start^goal
        cnt=0
        while xor>0:
            cnt+=xor&1
            xor>>=1
        return cnt
