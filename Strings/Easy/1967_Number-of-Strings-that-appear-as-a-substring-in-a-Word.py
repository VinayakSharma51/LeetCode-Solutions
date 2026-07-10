# LeetCode 1967: Number of Strings That Appear as Substrings in Word
# Difficulty: Easy
# Topic: String

# Approach:
# - Traverse every string in the patterns array.
# - Check if the current pattern exists as a substring
#   in the given word.
# - If it exists, increase the count.
# - Return the total number of matching patterns.

# This is the optimal solution.

# Time Complexity: O(n × m)
# where:
# n = number of patterns
# m = length of the word

# Space Complexity: O(1)

class Solution(object):
    def numOfStrings(self, patterns, word):

        # Stores the number of matching patterns.
        output = 0

        # Check every pattern one by one.
        for pattern in patterns:

            # If the pattern is found in the word,
            # increase the count.
            if pattern in word:
                output += 1

        # Return the total number of patterns found.
        return output