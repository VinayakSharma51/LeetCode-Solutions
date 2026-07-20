# LeetCode 1260: Shift 2D Grid
# Difficulty: Easy
# Topic: Array, Matrix

# Approach:
# - Flatten the 2D grid into a 1D list.
# - Reduce k using modulo to avoid unnecessary shifts.
# - Perform the shift by slicing the flattened list.
# - Reconstruct the shifted 1D list back into
#   a 2D grid with the original number of columns.

# This is the optimal solution.

# Time Complexity: O(m × n)
# where:
# m = number of rows
# n = number of columns

# Space Complexity: O(m × n)

class Solution(object):
    def shiftGrid(self, grid, k):

        # Convert the 2D grid into a 1D list.
        flattened = [num for row in grid for num in row]

        # Number of columns in the original grid.
        cols = len(grid[0])

        # Stores the final shifted grid.
        result = []

        # Reduce k since shifting by the grid size
        # results in the original grid.
        k %= len(flattened)

        # Shift the flattened list to the right.
        shifted = flattened[-k:] + flattened[:-k]

        # Rebuild the 2D grid using the original
        # number of columns.
        for i in range(0, len(shifted), cols):
            result.append(shifted[i:i + cols])

        # Return the shifted grid.
        return result