class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        s = sorted(nums)
        output = set()
        for i in range(len(s)):
            for j in range(len(s)):
                if i == j:
                    continue
                current_target = target -(s[i]+s[j])
                k,l = i+1, len(s)-1
                while k < l:
                    if k == j:
                        k += 1
                        continue
                    if l == j:
                        l -= 1
                        continue
                    sum_two = s[k] + s[l]
                    if sum_two < current_target:
                        k += 1
                    elif sum_two > current_target:
                        l -= 1
                    else:
                        output.add(tuple(sorted([s[i],s[j],s[k], s[l]])))
                        k += 1
                        l -= 1
        return output