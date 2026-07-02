# LeetCode 9: Palindrome Number
# Difficulty: Easy
# Topic: Math
#
# Approach:
# - Reverse only half of the number instead of the entire number.
# - Compare the first half with the reversed second half.
#
# This is the optimal solution.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution(object):
    def isPalindrome(self, x):
        # Negative numbers and numbers ending with 0
        # (except 0 itself) cannot be palindromes.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverse = 0

        # Reverse only half of the digits.
        while x > reverse:
            reverse = reverse * 10 + x % 10
            x //= 10

        # Even number of digits:
        # x == reverse
        #
        # Odd number of digits:
        # Ignore the middle digit using reverse // 10
        return x == reverse or x == reverse // 10
