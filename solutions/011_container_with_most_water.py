from functools import lru_cache

class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        max_area = 0

        while end > start:
            max_area = max(max_area, min(height[start], height[end]) * (end - start))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return max_area

    # def maxArea(self, height: List[int]) -> int:
    #     @lru_cache(maxsize=None)
    #     def dp(i, j):
    #         if i == j:
    #             return 0
    #         else:
    #             value = min(height[i-1], height[j-1]) * (j-i)
    #             if height[i-1] <= height[j-1]:
    #                 next_content = dp(i+1,j)
    #             else:
    #                 next_content = dp(i,j-1)
    #             return max(value, next_content)
    #     return dp(1,len(height))