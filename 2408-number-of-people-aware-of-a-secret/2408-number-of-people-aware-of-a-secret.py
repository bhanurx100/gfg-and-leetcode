class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        mod = 10**9 + 7
        dp = [0] * (n + 1)  # dp[i] = number of people who learn the secret on day i
        dp[1] = 1

        noOfPeopleWithSecret = 0  # running count of people who can share

        for i in range(2, n + 1):
            # People who learned 'delay' days ago start sharing today
            noOfNewPeopleWithSecret = dp[i - delay] if i - delay >= 1 else 0

            # People who learned 'forget' days ago forget today
            noOfPeopleForgetSecret = dp[i - forget] if i - forget >= 1 else 0

            # Update active sharers
            noOfPeopleWithSecret = (noOfPeopleWithSecret + noOfNewPeopleWithSecret - noOfPeopleForgetSecret + mod) % mod

            # The number of new people learning today equals the number of people sharing
            dp[i] = noOfPeopleWithSecret

        # Sum up those who still remember on day n
        ans = 0
        for i in range(n - forget + 1, n + 1):
            if i >= 1:
                ans = (ans + dp[i]) % mod

        return ans