class Solution:
    def putMarbles(self, w: List[int], k: int) -> int:
        p = sorted([w[i] + w[i + 1] for i in range(len(w) - 1)])
        return sum(p[len(p) - k + 1:]) - sum(p[:k - 1])