# LeetCode 20: Valid Parentheses
# Difficulty: Easy
# Topic: String, Stack

# Approach:
# - Use a stack to keep track of opening brackets.
# - Push every opening bracket onto the stack.
# - For every closing bracket, check if it matches
#   the most recent opening bracket.
# - If it doesn't match or the stack is empty,
#   the string is invalid.
# - At the end, the stack should be empty for
#   the string to be valid.

# This is the optimal solution.

# Time Complexity: O(n)
# where:
# n = length of the string

# Space Complexity: O(n)

class Solution(object):
    def isValid(self, s):

        # Stores the matching closing bracket
        # for every opening bracket.
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        # Stack to keep track of opening brackets.
        stack = []

        # Traverse each character in the string.
        for char in s:

            # If it is an opening bracket,
            # push it onto the stack.
            if char in pairs:
                stack.append(char)

            else:
                # If there is no opening bracket
                # available to match, return False.
                if not stack:
                    return False

                # Check if the current closing bracket
                # matches the last opening bracket.
                if pairs[stack[-1]] != char:
                    return False

                # Matching pair found, so remove it.
                stack.pop()

        # The string is valid only if
        # no unmatched opening brackets remain.
        return not stack