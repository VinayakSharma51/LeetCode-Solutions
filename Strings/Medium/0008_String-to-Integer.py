# LeetCode 8: String to Integer (atoi)
# Difficulty: Medium
# Topic: String, Math

# Approach:
# - Skip all leading whitespace characters.
# - Check for an optional '+' or '-' sign.
# - Read the digits one by one and build the integer.
# - Before adding each digit, check whether the result
#   would overflow the 32-bit signed integer range.
# - Return the clamped value if overflow occurs.
# - Otherwise, return the final signed integer.

# This is the optimal solution.

# Time Complexity: O(n)
# where: n = length of the input string

# Space Complexity: O(1)

class Solution(object):
    def myAtoi(self, s):

        # Define the 32-bit signed integer range.
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Initialize variables.
        i = 0
        n = len(s)
        sign = 1
        num = 0

        # Skip leading whitespace characters.
        while i < n and s[i] == ' ':
            i += 1

        # If the string contains only spaces,
        # return 0.
        if i == n:
            return 0

        # Check for an optional sign.
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

        # Process each digit.
        while i < n and s[i].isdigit():

            # Convert the current character to an integer.
            digit = int(s[i])

            # Check if adding this digit would cause
            # a 32-bit integer overflow.
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            # Build the number.
            num = num * 10 + digit

            # Move to the next character.
            i += 1

        # Apply the sign and return the result.
        return sign * num