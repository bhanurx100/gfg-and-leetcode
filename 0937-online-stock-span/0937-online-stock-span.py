class StockSpanner:

    def __init__(self):
        # Stack to store pairs of (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        # Initialize the span for the current price as 1
        span = 1
        
        # While the stack is not empty and the price at the top of the stack
        # is less than or equal to the current price, pop from the stack
        # and add the span of the popped element to the current span
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        
        # Push the current price and its span onto the stack
        self.stack.append((price, span))
        
        # Return the span for the current price
        return span
