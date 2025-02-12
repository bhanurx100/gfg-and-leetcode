from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)  # Convert list to set for O(1) lookup
        if endWord not in wordSet:
            return 0  # If endWord is not in wordList, no transformation possible

        queue = deque([(beginWord, 1)])  # BFS queue: (current_word, depth)
        
        while queue:
            current_word, level = queue.popleft()  # Get the front element
            
            # Try changing each character in the word
            for i in range(len(current_word)):
                original_char = current_word[i]
                
                for c in 'abcdefghijklmnopqrstuvwxyz':  # Try all letters 'a' to 'z'
                    if c == original_char:
                        continue  # Skip the same character
                    
                    new_word = current_word[:i] + c + current_word[i+1:]  # Replace character
                    
                    if new_word == endWord:
                        return level + 1  # Found the shortest path
                    
                    if new_word in wordSet:  # If valid transformation
                        queue.append((new_word, level + 1))
                        wordSet.remove(new_word)  # Remove to prevent duplicate visits
        
        return 0  # If no path is found
