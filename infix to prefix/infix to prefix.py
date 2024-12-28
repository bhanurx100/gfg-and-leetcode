class Solution:
    def InfixtoPostfix(self, s):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        stack = []
        result = ""

        for char in s:
            if char.isalnum():  # If operand, add to result
                result += char
            elif char == '(':  # Push opening parenthesis
                stack.append(char)
            elif char == ')':  # Pop until opening parenthesis
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()  # Remove '(' from the stack
            else:  # Operator
                while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence[char]:
                    result += stack.pop()
                stack.append(char)

        # Pop remaining operators
        while stack:
            result += stack.pop()

        return result
