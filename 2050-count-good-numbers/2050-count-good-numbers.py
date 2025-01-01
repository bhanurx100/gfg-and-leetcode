class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD=10**9+7
        def mod_exp(base,exp,mod):
            res=1
            while exp>0:
                if exp%2==1:
                    res=(res*base)%mod
                base=(base*base)%mod
                exp//=2
            return res
        even_count=(n+1)//2
        odd_count=n//2
        even_res=mod_exp(5,even_count,MOD)
        odd_res=mod_exp(4,odd_count,MOD)
        return (even_res*odd_res)%MOD