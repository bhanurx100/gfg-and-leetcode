class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        Remove k digits from the number string `num` to form the smallest possible integer.
        
        :param num: String representing a non-negative integer.
        :param k: Number of digits to remove.
        :return: Smallest possible integer as a string.
        """
        # Stack to store the digits of the resulting number
        stack = []
        
        # Iterate over each digit in the input number
        for digit in num:
            # Remove digits from the stack if:
            # 1. There are still digits left to remove (k > 0)
            # 2. The top of the stack is greater than the current digit (to form a smaller number)
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            
            # Append the current digit to the stack
            stack.append(digit)
        
        # If k > 0, remove the remaining digits from the end of the stack
        while k > 0:
            stack.pop()
            k -= 1
        
        # Convert the stack into the result string
        result = ''.join(stack)
        
        # Remove leading zeros, if any, and return "0" if the result is empty
        return result.lstrip('0') or "0"
