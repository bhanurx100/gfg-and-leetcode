class MinStack:
    def __init__(self):
        # Main stack to store elements
        self.stack = []
        # Auxiliary stack to store the minimums
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push the new minimum to the min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            # Keep the previous minimum
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        # Pop from both stacks
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        # Return the top element of the main stack
        if self.stack:
            return self.stack[-1]
        return -1  # Return -1 if the stack is empty (optional)

    def getMin(self) -> int:
        # Return the top element of the min_stack
        if self.min_stack:
            return self.min_stack[-1]
        return -1  # Return -1 if the min_stack is empty (optional)


