# LeetCode 14: Longest Common Prefix
# Difficulty: Easy
# Topic: String

# Approach:
# - Assume the first string is the common prefix.
# - Compare it with every other string.
# - If the current string does not start with the prefix,
#   remove the last character from the prefix.
# - Continue until a common prefix is found or the prefix becomes empty.

# This is the optimal solution.

# Time Complexity: O(n * m)
# where:
# n = number of strings
# m = length of the longest common prefix

# Space Complexity: O(1)

class Solution(object):
    def longestCommonPrefix(self, strs):

        # If the list is empty, there is no common prefix.
        if not strs:
            return ""

        # Assume the first string is the longest common prefix.
        prefix = strs[0]

        # Compare the prefix with every remaining string.
        for s in strs[1:]:

            # Keep reducing the prefix until
            # the current string starts with it.
            while not s.startswith(prefix):
                prefix = prefix[:-1]

                # If the prefix becomes empty,
                # no common prefix exists.
                if not prefix:
                    return ""

        # Return the longest common prefix.
        return prefix