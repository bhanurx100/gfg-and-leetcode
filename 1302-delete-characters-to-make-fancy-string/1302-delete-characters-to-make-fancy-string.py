class Solution:
    def makeFancyString(self, s: str) -> str:
        ans=[]
        last=s[0]
        ans.append(last)
        cnt=1
        for i in range(1,len(s)):
            if s[i]==last:
                cnt+=1
                if cnt<3:
                    ans.append(s[i])
            else:
                last=s[i]
                cnt=1
                ans.append(s[i])
        return "".join(ans)