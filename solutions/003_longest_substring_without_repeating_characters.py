from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substring_length = 0
        current_substring = deque([])
        current_substring_set = set()
        for char in s:
            if char in current_substring_set:
                while char in current_substring_set:
                    char_bis = current_substring.popleft()
                    current_substring_set.remove(char_bis)
    
            current_substring.append(char)
            current_substring_set.add(char)
            
            if len(current_substring_set) > max_substring_length:
                max_substring_length = len(current_substring_set)
        return max_substring_length