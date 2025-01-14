class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals by their end time
        intervals.sort(key=lambda x: x[1])        
        last_end = float('-inf')  # Initialize last_end to negative infinity
        non_overlapping = 0       # Counter for non-overlapping intervals        
        for start, end in intervals:
            # If current interval does not overlap with the last one
            if start >= last_end:
                non_overlapping += 1
                last_end = end  # Update last_end to the current interval's end time        
        # Total intervals minus non-overlapping gives the count of removals
        return len(intervals) - non_overlapping
