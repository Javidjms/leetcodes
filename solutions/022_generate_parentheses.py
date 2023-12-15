from functools import lru_cache
from itertools import product

class Solution:
    @lru_cache(maxsize = None) 
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        else:
            output_set = set()
            for i in range(1, n):
                for x,y in product(self.generateParenthesis(n-i), self.generateParenthesis(i)):
                    output_set.add(f"{x}{y}")
                    if i == 1:
                        output_set.add(f"({x})")
            return list(output_set)
        