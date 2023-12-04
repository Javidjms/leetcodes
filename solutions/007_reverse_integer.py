class Solution:
    def reverse(self, x: int) -> int:
        is_signed = x < 0
        reversed_int = int(str(abs(x))[::-1]) * (-1 if is_signed else 1)
        if reversed_int < -2**31 or reversed_int > 2**31-1:
            return 0
        return reversed_int
        