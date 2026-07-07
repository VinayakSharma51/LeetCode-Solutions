# LeetCode 3754: Concatenate Non-Zero Digits and Multiply by Sum I
# Difficulty: Easy
# Topic: Math

# Approach:
# - Convert the number to a string.
# - Ignore all '0' digits and store the remaining digits.
# - Concatenate the non-zero digits to form a new number.
# - Calculate the sum of the non-zero digits.
# - Return the product of the new number and the digit sum.

# This is an optimal solution.

# Time Complexity: O(n)
# where:
# n = number of digits in the input number

# Space Complexity: O(n)

class Solution(object):
    def sumAndMultiply(self, n):

        # If the number is 0, the answer is 0.
        if n == 0:
            return 0

        # Store all non-zero digits.
        digits = []

        # Ignore every '0' while traversing the number.
        for ch in str(n):
            if ch != '0':
                digits.append(ch)

        # Form the new number by joining the remaining digits.
        x = int("".join(digits))

        # Calculate the sum of the remaining digits.
        digit_sum = 0
        for digit in digits:
            digit_sum += int(digit)

        # Return the required result.
        return x * digit_sum