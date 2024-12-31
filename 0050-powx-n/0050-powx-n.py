class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle the case where n is negative
        if n < 0:
            x = 1 / x
            n = -n
        
        def fast_pow(base, exp):
            if exp == 0:
                return 1
            half = fast_pow(base, exp // 2)
            if exp % 2 == 0:
                return half * half
            else:
                return half * half * base
        
        return fast_pow(x, n)
