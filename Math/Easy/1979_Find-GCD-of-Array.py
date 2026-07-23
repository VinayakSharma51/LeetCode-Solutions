# LeetCode 1979: Find Greatest Common Divisor of Array
# Difficulty: Easy
# Topic: Array, Math, Number Theory

# Approach:
# - Find the smallest and largest elements in the array.
# - Use the Euclidean Algorithm to compute their GCD.
# - Keep replacing:
#     largest = smallest
#     smallest = largest % smallest
#  + until the remainder becomes 0.
# - The last non-zero value is the GCD.

# This is the optimal solution.

# Time Complexity: O(n + log m)
# where: n = number of elements in the array
# m = value of the largest element

# Space Complexity: O(1)

class Solution(object):
    def findGCD(self, nums):

        # Find the largest and smallest numbers.
        largest = max(nums)
        smallest = min(nums)

        # Apply the Euclidean Algorithm.
        while smallest:

            # Update the values:
            # - largest becomes the previous smallest.
            # - smallest becomes the remainder.
            largest, smallest = smallest, largest % smallest

        # The last non-zero value is the GCD.
        return largest
