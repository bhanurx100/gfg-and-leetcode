class Solution:
    def Sorted(self, s):
        # Temporary stack to maintain sorted order
        temp_stack = []
        
        while s:
            # Pop the top element from the input stack
            current = s.pop()
            
            # Maintain decreasing order in the temp_stack
            # If the top of temp_stack is smaller than current, move elements back to s
            while temp_stack and temp_stack[-1] < current:
                s.append(temp_stack.pop())
            
            # Push the current element onto temp_stack
            temp_stack.append(current)
        
        # Copy elements back to the original stack (now sorted in decreasing order)
        while temp_stack:
            s.append(temp_stack.pop())

# Example Usage
if __name__ == "__main__":
    stack = [11, 2, 32, 3, 41]
    solution = Solution()
    solution.Sorted(stack)
    print(stack)  # Output: [41, 32, 11, 3, 2]
