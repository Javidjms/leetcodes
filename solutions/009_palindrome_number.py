class Solution:
    def isPalindrome(self, x: int) -> bool:
        number_str = str(x)
        return number_str == number_str[::-1]
        