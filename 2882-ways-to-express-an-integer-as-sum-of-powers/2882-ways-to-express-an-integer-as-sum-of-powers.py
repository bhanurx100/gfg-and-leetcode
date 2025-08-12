from typing import List

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 1_000_000_007  

        # Precompute powers: 1^x, 2^x, ..., k^x <= n
        powers = []
        i = 1
        while True:
            p = i ** x
            if p > n:
                break
            powers.append(p)
            i += 1

        # dp[s] = number of ways to make sum s using a subset of `powers`
        dp = [0] * (n + 1)
        dp[0] = 1  # one way to make 0: pick nothing

        # 0/1 knapsack: iterate sums downward to avoid reusing the same power
        for p in powers:
            for s in range(n, p - 1, -1):
                dp[s] = (dp[s] + dp[s - p]) % MOD

        return dp[n]