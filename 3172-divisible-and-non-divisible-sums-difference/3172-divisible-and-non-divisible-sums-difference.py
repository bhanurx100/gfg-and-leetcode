class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        #(total−divisibleSum)−divisibleSum=total−2divisibleSum.
        return n*(n+1)//2-2*m*(n//m*(n//m+1)//2)