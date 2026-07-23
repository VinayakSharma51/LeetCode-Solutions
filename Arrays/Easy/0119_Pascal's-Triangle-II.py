# LeetCode 119: Pascal's Triangle II
# Difficulty: Easy
# Topic: Array, Dynamic Programming

# Approach:
# - Start with the first row [1].
# - Generate each next row using the previous row.
# - Every row starts and ends with 1.
# - Each middle element is the sum of the two adjacent elements from the previous row.
# - Repeat until the required row index is reached.

# This is the optimal solution.

# Time Complexity: O(n²)
# where: n = rowIndex

# Space Complexity: O(n)

class Solution(object):
    def getRow(self, rowIndex):

        # The first row of Pascal's Triangle.
        row = [1]

        # Generate rows until the required row is reached.
        for _ in range(rowIndex):

            # Every new row starts with 1.
            new_row = [1]

            # Generate the middle elements by adding
            # adjacent elements from the previous row.
            for i in range(len(row) - 1):
                new_row.append(row[i] + row[i + 1])

            # Every row ends with 1.
            new_row.append(1)

            # Update the current row.
            row = new_row

        # Return the required row.
        return row