class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        real_num = n - k
        mod = int(1e9)+7
        num_ways = (m * pow((m-1),(real_num-1),mod))%mod
        res = num_ways * math.comb(real_num + k-1, real_num-1)
        res%=mod
        return int(res)