import heapq

class Solution:
    def maxAverageRatio(self, classes, extraStudents: int) -> float:
        def gain(pass_count, total_count):
            return (pass_count + 1) / (total_count + 1) - pass_count / total_count

        heap = []
        total_sum = 0.0
        for p, t in classes:
            total_sum += p / t
            heapq.heappush(heap, (-gain(p, t), p, t))  # max heap with negated gain

        while extraStudents > 0:
            g, p, t = heapq.heappop(heap)
            total_sum -= p / t
            p += 1; t += 1
            total_sum += p / t
            heapq.heappush(heap, (-gain(p, t), p, t))
            extraStudents -= 1

        return total_sum / len(classes)