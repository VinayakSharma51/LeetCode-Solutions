# LeetCode 7: Reverse Integer
# Difficulty: Medium
# Topic: Math
#
# Approach:
# - Extract the last digit of the number one by one.
# - Build the reversed number by appending each digit.
# - Restore the original sign if the number was negative.
# - Check whether the reversed number is within
#   the 32-bit signed integer range.
# - If it is outside the range, return 0.
#
# Time Complexity: O(log n)
# where:
# n = absolute value of the input number
#
# Space Complexity: O(1)

class Solution(object):
    def reverse(self, x):

        # Define the 32-bit signed integer range.
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        # Check whether the number is negative.
        is_negative = x < 0

        # Work with the absolute value.
        x = abs(x)

        # Stores the reversed number.
        rev_x = 0

        # Reverse the number digit by digit.
        while x > 0:

            # Extract the last digit.
            digit = x % 10

            # Append the digit to the reversed number.
            rev_x = rev_x * 10 + digit

            # Remove the last digit from the original number.
            x //= 10

        # Restore the negative sign if needed.
        if is_negative:
            rev_x *= -1

        # Return 0 if the reversed number
        # is outside the 32-bit integer range.
        if rev_x < INT_MIN or rev_x > INT_MAX:
            return 0

        # Return the reversed integer.
        return rev_x