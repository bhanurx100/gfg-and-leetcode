class Solution:
    def splitArray(self, nums: List[int]) -> int:
        def is_prime(n):
            if n<2:
                return False
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
            return True
        A,B=0,0
        for i,num in enumerate(nums):
            if is_prime(i):
                A+=num
            else:
                B+=num
        return abs(A-B)