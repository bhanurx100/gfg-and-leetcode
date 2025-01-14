class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        n, m=len(g), len(s)
        l, r=0, 0
        g.sort(), s.sort()
        while l<n and r<m:
            if g[l]<=s[r]:
                l+=1
            r+=1

        return l