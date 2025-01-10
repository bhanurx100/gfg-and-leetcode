class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        task_counts = Counter(tasks)
        max_freq = max(task_counts.values())  # Highest frequency of any task
        max_count = sum(1 for task in task_counts.values() if task == max_freq)  # Number of tasks with max frequency
        
        # Calculate the minimum intervals using the formula
        part_count = max_freq - 1  # Number of full parts
        part_length = n - (max_count - 1)  # Available slots in each part
        empty_slots = part_count * part_length  # Total empty slots
        remaining_tasks = len(tasks) - (max_freq * max_count)  # Tasks to fill the empty slots
        idles = max(0, empty_slots - remaining_tasks)  # Idle slots if remaining tasks can't fill all
        
        return len(tasks) + idles