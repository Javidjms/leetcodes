class Solution:
    def get_largest_palindrome(self, s, start, end):
        large = ""
        while start >= 0 and end <= len(s) and s[start] == s[end-1]:
            if len(s[start:end]) > len(large):
                large = s[start:end]
            start -=1
            end +=1
        return large

    def longestPalindrome(self, s: str) -> str:
        largest_palindrome = ""
        for i in range(len(s)):
            large1 = self.get_largest_palindrome(s, i,i+1)
            large2 = self.get_largest_palindrome(s, i,i+2)
            largest_palindrome = max(large1, large2, largest_palindrome, key=len)
        return largest_palindrome