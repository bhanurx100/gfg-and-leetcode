from typing import List

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # Convert n to its canonical "sorted-digit string" representation.
        # Example: n = 128 -> "128" -> sorted -> ['1','2','8'] -> "128"
        n_sorted = "".join(sorted(str(n)))

        # Precompute the sorted-digit strings for powers of two.
        # 2**0, 2**1, ..., 2**30 covers up to 10^9 (and beyond for typical constraints).
        powers_sorted = set()
        for i in range(31):
            p = 1 << i                    # compute 2**i
            powers_sorted.add("".join(sorted(str(p))))

        # If the sorted-digit string of n matches any precomputed one, some permutation is a power of two.
        return n_sorted in powers_sorted
