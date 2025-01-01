class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(current, open_count, close_count):
            # Base case: if the current string has 2 * n characters, add it to the result
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # Add an open parenthesis if we have not used n open parentheses
            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)
            
            # Add a close parenthesis if there are more open parentheses than close parentheses
            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)
        
        result = []
        backtrack("", 0, 0)  # Initial call to backtrack
        return result