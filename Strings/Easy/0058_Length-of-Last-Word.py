# LeetCode 58: Length of Last Word
# Difficulty: Easy
# Topic: String
#
# Approach:
# - Start from the end of the string.
# - Skip all trailing spaces.
# - Count the characters until a space
#   or the beginning of the string is reached.
# - Return the length of the last word.
#
# This is the optimal solution.
#
# Time Complexity: O(n)
# where:
# n = length of the string
#
# Space Complexity: O(1)

class Solution(object):

    def lengthOfLastWord(self, s):

        # Start from the last character.
        i = len(s) - 1

        # Skip any trailing spaces.
        while i >= 0 and s[i] == ' ':
            i -= 1

        # Stores the length of the last word.
        length = 0

        # Count characters until a space
        # or the beginning of the string.
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        # Return the length of the last word.
        return length