class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10**9 + 7
        if not word:
            return 0

        # Count groups of repeated characters
        groups = []
        count = 1
        for i in range(1, len(word)):
            if word[i] == word[i-1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count)

        total = 1
        for g in groups:
            total = (total * g) % MOD

        if k <= len(groups):
            return total

        dp = [0] * k
        dp[0] = 1

        for g in groups:
            new_dp = [0] * k
            sum_ = 0
            for s in range(k):
                if s > 0:
                    sum_ = (sum_ + dp[s-1]) % MOD
                if s > g:
                    sum_ = (sum_ - dp[s - g - 1] + MOD) % MOD
                new_dp[s] = sum_
            dp = new_dp

        invalid = sum(dp[len(groups):]) % MOD
        return (total - invalid + MOD) % MOD