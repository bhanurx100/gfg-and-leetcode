MOD = 10**9 + 7


class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:

        # precompute divisors
        divisors = [[] for _ in range(maxValue + 1)]
        for i in range(1, maxValue + 1):
            for j in range(i, maxValue + 1, i):
                divisors[j].append(i)

        # dirichlet convolution
        def dconv(x, y):
            return [0] + [
                sum(x[d] * y[m // d] for d in divisors[m]) % MOD
                for m in range(1, maxValue + 1)
            ]

        # fast exponentiation of convolution
        base = [1] * (maxValue + 1)
        result = [0] * (maxValue + 1)
        result[1] = 1

        while n:
            if n & 1:
                result = dconv(result, base)
            base = dconv(base, base)
            n >>= 1

        return sum(result[1:]) % MOD