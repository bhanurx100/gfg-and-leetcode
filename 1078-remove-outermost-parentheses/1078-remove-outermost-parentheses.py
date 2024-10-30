class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        popen, result = 0, []
        for x in S:
            if x==')':
                popen -= 1
            if popen>0:
                result.append(x)
            if x=='(':
                popen += 1
        return ''.join(result)