# LeetCode 1: Two Sum
# Difficulty: Easy
# Topic: Array, Hash Table
#
# Approach:
# - Use a hash map (dictionary) to store each number along with its index.
# - For every number, calculate the remaining value needed to reach the target.
# - If the remaining value has already been seen, return both indices.
# - Otherwise, store the current number and continue.
#
# This is the optimal solution.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def twoSum(self, nums, target):
        # Dictionary to store:
        # Number -> Index
        seen = {}

        # Traverse the array once
        for index, value in enumerate(nums):

            # Find the number needed to reach the target
            remain = target - value

            # If the required number already exists,
            # we have found the answer.
            if remain in seen:
                return [seen[remain], index]

            # Store the current number and its index
            # for future lookups.
            seen[value] = index
