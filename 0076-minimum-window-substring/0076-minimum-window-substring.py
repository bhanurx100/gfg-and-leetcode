class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        # Count the frequency of characters in t
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
        
        # Variables for the sliding window
        left = 0
        min_len = float('inf')
        min_start = 0
        required = len(t_count)
        formed = 0
        window_count = {}
        
        # Slide the right pointer
        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            
            # Check if the current character meets the requirement
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1
            
            # When the window is valid, try to shrink it
            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left
                
                # Remove the leftmost character from the window
                left_char = s[left]
                window_count[left_char] -= 1
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    formed -= 1
                
                left += 1
        
        return s[min_start:min_start + min_len] if min_len != float('inf') else ""
