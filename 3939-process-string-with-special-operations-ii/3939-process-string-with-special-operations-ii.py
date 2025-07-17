class Solution:
    def processStr(self, s: str, k: int) -> str:
        # First pass: compute final length after all operations
        str_len = 0
        for ch in s:
            if ch.islower():
                str_len += 1
            elif ch == '*' and str_len > 0:
                str_len -= 1
            elif ch == '#':
                str_len *= 2
            # elif ch == '%':
            #     pass  # No length change
        
        # Convert k to 1-based per problem statement
        if k < 0 or k >= str_len:
            return '.'
        #k -= 1  # make 0-based for easier math

        # Second pass: reverse simulation to find the k-th char
        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            if ch.islower():
                str_len -= 1
                if k == str_len:
                    return ch
            elif ch == '*':
                str_len += 1  # Undo removal, so +1
            elif ch == '#':
                # Duplication doubled the length, so restore k and str_len
                if k >= str_len // 2:
                    k -= str_len // 2
                str_len //= 2
            elif ch == '%':
                # Undo reversal
                k = str_len - k - 1

        return '.'
