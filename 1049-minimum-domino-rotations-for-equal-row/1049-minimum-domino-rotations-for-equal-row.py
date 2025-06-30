class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        res = self.getRotation(tops, bottoms, tops[0])
        if bottoms[0] != tops[0]:
            res = min(res, self.getRotation(tops, bottoms, bottoms[0]))
        return -1 if res == float('inf') else res

    def getRotation(self, tops, bottoms, target):
        rotateTop = rotateBottom = 0
        for i in range(len(tops)):
            if tops[i] != target and bottoms[i] != target:
                return float('inf')
            elif tops[i] != target:
                rotateTop += 1
            elif bottoms[i] != target:
                rotateBottom += 1
        return min(rotateTop, rotateBottom)
