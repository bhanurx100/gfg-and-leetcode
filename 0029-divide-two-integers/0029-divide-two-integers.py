class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX,INT_MIN=2**31-1,-2**31
        if dividend==INT_MIN and divisor==-1:
            return INT_MAX
        negative=(dividend<0)^(divisor<0)
        dividend,divisor=abs(dividend),abs(divisor)
        quotient=0
        while dividend>=divisor:
            temp_divisor,multiple=divisor,1
            while dividend>=(temp_divisor<<1):
                temp_divisor<<=1
                multiple<<=1
            dividend-=temp_divisor
            quotient+=multiple
        if negative:
            quotient=-quotient
        return max(INT_MIN,min(INT_MAX,quotient))