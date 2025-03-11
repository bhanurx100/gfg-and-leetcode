class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        dp = [None] * 3
        result = 0
        for i in range(len(s)):
            # ord(s[i]) convert to ASCII code, a,b,c = 97,98,99 
            # -> ord(s[i] - 97) means that a,b,c = 0,1,2
            # Additionally, I store i+1 instead of +1 when calculating and conveniently using all() function.
            dp[ord(s[i])-97] = i+1
            if all(dp):
                result += min(dp)
        return result