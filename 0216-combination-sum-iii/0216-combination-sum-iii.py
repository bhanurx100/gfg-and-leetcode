class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(start, path, total):
            if len(path) == k:
                if total == n:
                    res.append(path[:])
                return

            for i in range(start, 10):  # 1 to 9
                if total + i > n:
                    break
                path.append(i)
                backtrack(i + 1, path, total + i)
                path.pop()

        backtrack(1, [], 0)
        return res
