# LeetCode 27: Remove Element
# Difficulty: Easy
# Topic: Array, Two Pointers
#
# Approach:
# - Traverse the array using a pointer.
# - If the current element is equal to 'val',
#   replace it with the last valid element in the array.
# - Reduce the valid array size by one.
# - If the current element is not equal to 'val',
#   move to the next index.
# - Continue until all valid elements have been checked.
#
# This is the optimal solution.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def removeElement(self, nums, val):

        # Pointer to traverse the array
        i = 0

        # Current valid size of the array
        n = len(nums)

        # Process only the valid part of the array
        while i < n:

            # If the current element matches 'val',
            # replace it with the last valid element.
            if nums[i] == val:
                nums[i] = nums[n - 1]

                # Reduce the valid array size.
                # No need to increase 'i' because the
                # swapped element still needs to be checked.
                n -= 1

            else:
                # Move to the next element
                # only if no replacement was made.
                i += 1

        # Return the number of valid elements.
        return n