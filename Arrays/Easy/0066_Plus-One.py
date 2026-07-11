# LeetCode 66: Plus One
# Difficulty: Easy
# Topic: Array, Math

# Approach:
# - Traverse the array from the last digit to the first.
# - If the current digit is less than 9,
#   simply increase it by 1 and return the result.
# - If the current digit is 9, change it to 0
#   and continue to the previous digit.
# - If all digits are 9, add 1 at the beginning
#   of the array.

# This is the optimal solution.

# Time Complexity: O(n)
# where:
# n = number of digits

# Space Complexity: O(1)
# (Ignoring the output array created when all digits are 9.)

class Solution(object):
    def plusOne(self, digits):

        # Traverse the array from right to left.
        for i in range(-1, -len(digits) - 1, -1):

            # If the current digit is less than 9,
            # increase it and return the answer.
            if digits[i] < 9:
                digits[i] += 1
                return digits

            # If the digit is 9, it becomes 0
            # and the carry moves to the previous digit.
            digits[i] = 0

        # If every digit was 9,
        # add 1 at the beginning.
        return [1] + digits