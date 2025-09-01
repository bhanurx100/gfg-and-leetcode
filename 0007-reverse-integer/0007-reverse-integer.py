class Solution:
    def reverse(self, x: int) -> int:
        mul=-1 if x<0 else 1
        x=abs(x)
        rev= int(str(x)[::-1])*mul
        if not ((-2**31//1)<=rev<=(2**31-1)//1):
            return 0
        return rev