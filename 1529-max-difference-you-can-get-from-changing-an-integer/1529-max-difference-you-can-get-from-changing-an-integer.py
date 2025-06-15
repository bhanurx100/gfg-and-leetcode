class Solution:
    def maxDiff(self, num: int) -> int:
        mx,mn=str(num),str(num)
        
        j=0
        while mx[j]=='9' and j<len(mx)-1:
            j+=1
        mx=mx.replace(mx[j],'9')

        for i in range(len(mn)):
            if i==0:
                if mn[i]!='1':
                    mn=mn.replace(mn[i],'1')
                    break
            else:
                if mn[i]!='0' and mn[i]!=mn[0]:
                    mn=mn.replace(mn[i],'0')
                    break

        return int(mx)-int(mn)