from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(maxsize=None)
        def dp(i, j):
            if j == len(p):
                return i == len(s)
            matched = i < len(s) and p[j] in (s[i], '.')
            if j+1 < len(p) and p[j+1] == "*":
                return dp(i, j+2) or matched and dp(i+1, j)
            else:
                return matched and dp(i+1, j+1)
        return dp(0,0)