from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Build the adjacency list representation of the graph
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)

        # Step 2: Initialize a list to track the state of each node during DFS
        # 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses

        # Step 3: Define the DFS function to detect cycles
        def hasCycle(v: int) -> bool:
            if state[v] == 1:  # Node is currently being visited, so a cycle is detected
                return True
            if state[v] == 2:  # Node has already been visited, no cycle from this node
                return False

            # Mark the node as visiting
            state[v] = 1
            # Recursively visit all the adjacent nodes
            for neighbor in graph[v]:
                if hasCycle(neighbor):
                    return True

            # Mark the node as visited after all its neighbors are processed
            state[v] = 2
            return False

        # Step 4: Check each course for cycles
        for course in range(numCourses):
            if hasCycle(course):
                return False  # Cycle detected, cannot finish all courses

        return True  # No cycles detected, can finish all courses
