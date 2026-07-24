# LeetCode 13: Roman to Integer
# Difficulty: Easy
# Topic: Hash Table, Math, String

# Approach:
# - Store the value of each Roman numeral in a hash map.
# - Traverse the string from right to left.
# - Keep track of the previous numeral's value.
# - If the current numeral is smaller than the previous one,
#   subtract it from the total.
# - Otherwise, add it to the total.
# - Return the final integer value.

# This is the optimal solution.

# Time Complexity: O(n)
# where: n = length of the Roman numeral string

# Space Complexity: O(1)

class Solution(object):
    def romanToInt(self, s):

        # Maps each Roman numeral to its integer value.
        nums = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Stores the final integer value.
        total = 0

        # Stores the value of the previous numeral.
        prev = 0

        # Traverse the string from right to left.
        for char in reversed(s):

            # Get the value of the current Roman numeral.
            curr = nums[char]

            # If the current value is smaller than the
            # previous value, subtract it.
            if curr < prev:
                total -= curr

            # Otherwise, add it to the total.
            else:
                total += curr

            # Update the previous value.
            prev = curr

        # Return the final integer.
        return total