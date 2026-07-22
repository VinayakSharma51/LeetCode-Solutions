# LeetCode 118: Pascal's Triangle
# Difficulty: Easy
# Topic: Array, Dynamic Programming

# Approach:
# - Start with an empty triangle.
# - The first row always contains a single 1.
# - For every new row:
#   - Begin and end the row with 1.
#   - Each middle element is the sum of the two adjacent elements from the previous row.
#   - Repeat until the required number of rows is generated.

# This is the optimal solution.

# Time Complexity: O(n²)
# where:
# n = number of rows

# Space Complexity: O(n²)
# (The output triangle itself stores all generated rows.)

class Solution(object):
    def generate(self, numRows):

        # Stores the complete Pascal's Triangle.
        triangle = []

        # Generate each row one by one.
        for row in range(numRows):

            # The first row always contains only 1.
            if row == 0:
                triangle.append([1])

            else:
                # Get the previous row.
                prev = triangle[-1]

                # Every row starts with 1.
                curr = [1]

                # Generate the middle elements by adding
                # adjacent elements from the previous row.
                for i in range(len(prev) - 1):
                    curr.append(prev[i] + prev[i + 1])

                # Every row ends with 1.
                curr.append(1)

                # Add the current row to the triangle.
                triangle.append(curr)

        # Return the completed Pascal's Triangle.
        return triangle