class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        result = []
        cur = 1

        for _ in range(n):  # n=102
            result.append(cur)  # 1 // 10 // 100 // 
            if cur * 10 <= n:  # 1000 // 1010
                # Move to the next level (next digit)
                cur *= 10  # 10 // 100 
            else:
                # Go back if cur exceeds n
                if cur >= n:
                    cur //= 10  # 1010 -> 101

                # Increment to the next number
                # e.g cur = 109
                cur += 1  # 101 // 102 

                # Handle ending with 9 or out of bounds
                # e.g. cur = 110
                while cur % 10 == 0:  # zero at 10 multipules
                    cur //= 10
                # e.g. cur = 11

        return result