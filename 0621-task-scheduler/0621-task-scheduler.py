from collections import Counter
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count the frequency of each task
        task_counts = Counter(tasks)
        
        # Step 2: Use a max heap to always select the task with the highest frequency
        # Python has a min-heap, so we store negative frequencies to simulate a max-heap
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)
        
        time = 0  # Initialize total time (intervals)

        # Step 3: Process tasks while the heap is not empty
        while max_heap:
            temp = []  # Temporarily store tasks for the current cycle
            cycle = 0  # Track how many tasks were processed in this cycle

            # Step 4: Execute up to n + 1 tasks in one cycle
            for _ in range(n + 1):
                if max_heap:
                    count = heapq.heappop(max_heap)  # Get the most frequent task
                    if count + 1 != 0:  # Decrease the count (since stored as negative)
                        temp.append(count + 1)  # If still remaining, add back to heap later
                    cycle += 1  # Increment tasks processed

            # Step 5: Push remaining tasks back into the heap
            for item in temp:
                heapq.heappush(max_heap, item)

            # Step 6: Increment time
            # If heap is empty, add only the actual tasks processed (no extra idle time)
            # If not, the cycle must be fully completed with idle slots
            time += cycle if not max_heap else n + 1

        return time
