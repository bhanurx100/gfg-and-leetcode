class Solution:
    def removeAnagrams(self, words):
        primes = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        mod = 1000000007

        def normal(s):
            res = 1
            for c in s:
                res = (res * primes[ord(c) - 97]) % mod
            return res

        res = [words[0]]
        prev = normal(words[0])

        for i in range(1, len(words)):
            key = normal(words[i])
            if key != prev:
                res.append(words[i])
                prev = key

        return res