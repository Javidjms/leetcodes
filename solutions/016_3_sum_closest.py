class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
      s = sorted(nums)
      closest = float('inf')
      for i in range(len(s)):
            current_target = target-s[i]
            j,k = i+1, len(s)-1
            while j < k:

                sum_two = s[j] + s[k]
                result = sum((s[i],s[j],s[k]))
                if abs(target-result) < abs(target-closest):
                    closest = result

                if sum_two <= current_target:
                    j += 1
                elif sum_two > current_target:
                    k -= 1
      
      return closest