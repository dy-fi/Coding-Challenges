# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

class Solution:
    def isPalindrome(self, x):
        x = str(x)
        return x == x[::-1]
        