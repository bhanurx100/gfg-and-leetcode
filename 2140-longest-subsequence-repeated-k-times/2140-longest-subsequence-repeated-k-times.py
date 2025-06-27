from collections import Counter, deque
import string

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        # Step 1. Filter eligible characters
        freq = Counter(s)
        char_list = [c for c in string.ascii_lowercase if freq[c] >= k]
        # Sort descending for lexicographical preference
        char_list.sort(reverse=True)

        # BFS queue starts with empty subsequence
        queue = deque([""])
        result = ""

        # Function to check if t * k is subsequence of s
        def is_valid(t: str) -> bool:
            repeat = t * k
            i = 0
            for ch in repeat:
                i = s.find(ch, i)  # fast built-in search
                if i == -1:
                    return False
                i += 1
            return True

        # BFS loop: builds t level by level
        while queue:
            curr = queue.popleft()
            # Prune: if even with full growth, cannot exceed current best
            if len(curr) * k + k > len(s):
                # since deeper levels only get longer, we're done
                continue
            for c in char_list:
                nxt = curr + c
                if is_valid(nxt):
                    queue.append(nxt)
                    # If longer or same-length but lex larger, update result
                    if len(nxt) > len(result) or (len(nxt) == len(result) and nxt > result):
                        result = nxt

        return result
