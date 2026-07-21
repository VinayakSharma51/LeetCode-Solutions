# LeetCode 1331: Rank Transform of an Array
# Difficulty: Easy
# Topic: Array, Sorting, Hash Table

# Approach:
# - Remove duplicate elements from the array.
# - Sort the unique elements in ascending order.
# - Assign a rank to each unique value starting from 1.
# - Replace every element in the original array
#   with its corresponding rank.

# This is the optimal solution.

# Time Complexity: O(n log n)
# where:
# n = number of elements in the array

# Space Complexity: O(n)

class Solution(object):
    def arrayRankTransform(self, arr):

        # Get all unique elements and sort them.
        sorted_unique = sorted(set(arr))

        # Maps each value to its rank.
        rank_map = {}

        # Assign ranks starting from 1.
        for index, value in enumerate(sorted_unique):
            rank_map[value] = index + 1

        # Replace each element with its rank.
        return [rank_map[num] for num in arr]