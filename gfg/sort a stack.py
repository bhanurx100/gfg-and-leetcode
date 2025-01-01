class Solution:
    # Recursive function to insert an element into the stack in decreasing order
    def insert_in_sorted_order(self, stack, element):
        # Base case: If the stack is empty or the top of the stack is greater than or equal to the element
        if not stack or stack[-1] <= element:
            stack.append(element)
            return
        
        # Remove the top element and recurse
        top = stack.pop()
        self.insert_in_sorted_order(stack, element)
        
        # Put the top element back
        stack.append(top)

    # Recursive function to sort the stack in decreasing order
    def Sorted(self, stack):
        # Base case: If the stack is empty
        if not stack:
            return
        
        # Remove the top element
        top = stack.pop()
        
        # Recursively sort the remaining stack
        self.Sorted(stack)
        
        # Insert the removed element back in sorted order
        self.insert_in_sorted_order(stack, top)

# Example Usage
if __name__ == "__main__":
    stack = [3, 2, 1]
    solution = Solution()
    solution.Sorted(stack)
    print(stack)  # Expected Output: [3, 2, 1]
