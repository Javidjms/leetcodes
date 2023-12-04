class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        scanned_numbers = dict()
        for index, num in enumerate(nums):
            if target-num in scanned_numbers:
                return [scanned_numbers[target-num], index]
            scanned_numbers[num] = index
