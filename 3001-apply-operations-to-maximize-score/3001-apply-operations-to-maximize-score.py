MX = 100001
MOD = 10**9 + 7
PSCORE = [0]*(MX)
for i in range(2, MX):
    if PSCORE[i] == 0:
        for j in range(i, MX, i):
            PSCORE[j] += 1

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        count = [1] * len(nums)
        stack = [(MX, -1)]
        for i, v in enumerate(nums):
            while stack[-1][0] < PSCORE[v]:
                _, j = stack.pop()
                count[j] *= i-j
            count[i] *= i-stack[-1][1]
            stack.append((PSCORE[v], i))

        while len(stack) > 1:
            _, j = stack.pop()
            count[j] *= len(nums)-j
        
        answer = 1
        for i in sorted(range(len(nums)), key=lambda x: nums[x], reverse=True):
            if k <= count[i]:
                answer = answer * pow(nums[i], k, MOD) % MOD
                break
            answer = answer * pow(nums[i], count[i], MOD) % MOD
            k -= count[i]
        return answer
                 