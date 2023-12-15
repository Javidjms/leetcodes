class Solution:
    def threeSum(self, nums):
      s = sorted(nums)
      output = set()
      for i in range(len(s)):
          target = -s[i]
          j,k = i+1, len(s)-1
          while j < k:
              sum_two = s[j] + s[k]
              if sum_two < target:
                  j += 1
              elif sum_two > target:
                  k -= 1
              else:
                  output.add((s[i],s[j],s[k]))
                  j += 1
                  k -= 1
      return output