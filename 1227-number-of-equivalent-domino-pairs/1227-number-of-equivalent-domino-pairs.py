class Solution:
        def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
            d = {}
            cnt = 0
            for a, b in dominoes:
                key = min(a, b) * 10 + max(a, b) 
                if key in d:
                    cnt += d[key] # the number of dominoes already in the map is the number of the newly found pairs.
                    d[key] += 1
                else:
                    d[key] = 1   
            return cnt  