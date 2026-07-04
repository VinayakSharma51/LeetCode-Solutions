# LeetCode 28: Find the Index of the First Occurrence in a String
# Difficulty: Easy
# Topic: String
#
# Approach:
# - Traverse the haystack string one character at a time.
# - At each position, compare the substring of length equal
#   to the needle with the needle itself.
# - If they match, return the current index.
# - If no match is found, return -1.
#
# This is a simple brute-force solution.
#
# Time Complexity: O((n - m + 1) * m)
# where:
# n = length of haystack
# m = length of needle
#
# In the worst case, this becomes O(n * m).
#
# Space Complexity: O(m)
# because Python creates a new substring when slicing.

class Solution(object):
    def strStr(self, haystack, needle):

        # An empty needle is always found at index 0.
        if needle == "":
            return 0

        # Check every possible starting position.
        for i in range(len(haystack)):

            # Compare the current substring with the needle.
            if haystack[i:i + len(needle)] == needle:
                return i

        # Needle was not found.
        return -1