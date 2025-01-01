class Solution:
    def count_NGEs(self, N, arr, queries, indices):
        # Function to count the number of greater elements to the right
        # N: Number of elements in the array
        # arr: The array of integers
        # queries: Number of queries
        # indices: The list of query indices

        # List to store the result for each query
        result = []

        # Process each query
        for idx in indices:
            # Initialize count of greater elements
            count = 0

            # Traverse the array from the index+1 to the end
            for i in range(idx + 1, N):
                # Check if the current element is greater than the queried element
                if arr[i] > arr[idx]:
                    count += 1
            
            # Append the count to the result
            result.append(count)

        return result
