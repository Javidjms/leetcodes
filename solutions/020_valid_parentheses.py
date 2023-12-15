from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        temp = deque([])
        opened_brackets_set = set(['(', '{', '['])
        closed_brackets_dict = {
            ')': '(', 
            '}': '{', 
            ']': '[', 
        }
        for c in s:
            if c in opened_brackets_set:
                temp.appendleft(c)
            elif len(temp) > 0 and c in closed_brackets_dict and temp[0] == closed_brackets_dict[c]:
                temp.popleft()
            else:
                return False
        return len(temp) == 0
        