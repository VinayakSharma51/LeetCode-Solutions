# LeetCode 35: Search Insert Position
# Difficulty: Easy
# Topic: Array, Binary Search

# Approach:
# - Use Binary Search to find the target element.
# - If the target is found, return its index.
# - If it is not found, the left pointer will indicate
#   the correct position where the target should be inserted.
# - Return the left pointer after the search ends.

# This is the optimal solution.

# Time Complexity: O(log n)
# where:
# n = number of elements in the array

# Space Complexity: O(1)

class Solution(object):
    def searchInsert(self, nums, target):

        # Initialize the search boundaries.
        left, right = 0, len(nums) - 1

        # Continue searching while the search space is valid.
        while left <= right:

            # Find the middle index.
            mid = (left + right) // 2

            # Target found.
            if nums[mid] == target:
                return mid

            # Search in the right half.
            elif nums[mid] < target:
                left = mid + 1

            # Search in the left half.
            else:
                right = mid - 1

        # If the target is not present,
        # left represents the correct insertion index.
        return left