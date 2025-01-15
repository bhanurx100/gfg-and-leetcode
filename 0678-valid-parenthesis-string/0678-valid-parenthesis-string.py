class Solution:
    def checkValidString(self, s: str) -> bool:
        l,r=0,0
        n=len(s)
        for char in s:
            if char=='(' or char=='*':
                l+=1
            else:
                l-=1
            if l<0:
                return False
        for char in reversed(s):
            if char==')' or char=='*':
                r+=1
            else:
                r-=1
            if r<0:
                return False
        return True