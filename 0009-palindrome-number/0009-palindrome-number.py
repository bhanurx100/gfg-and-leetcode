class Solution:
    def isPalindrome(self, x: int) -> bool:
        dup=x
        revnum=0
        while x>0:
            ld=x%10
            revnum=revnum*10+ld
            x=x//10
        if dup!=revnum:
            return False
        else:
            return True