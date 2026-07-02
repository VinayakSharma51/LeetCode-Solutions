# LeetCode 3: Longest Substring Without Repeating Characters
# Difficulty: Medium
# Topic: String, Hash Table, Sliding Window
#
# Approach:
# - Use the Sliding Window technique with a Hash Set.
# - Expand the window by moving the right pointer.
# - If a duplicate character is found, shrink the window
#   from the left until all characters are unique.
# - Keep track of the maximum window size.
#
# This is the optimal solution.
#
# Time Complexity: O(n)
# Space Complexity: O(min(n, m))
# where:
# n = length of the string
# m = size of the character set

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # Stores the unique characters in the current window
        seen = set()

        # Left pointer of the sliding window
        left = 0

        # Length of the longest valid substring found
        longest = 0

        # Expand the window one character at a time
        for right in range(len(s)):

            # If the current character already exists,
            # shrink the window until the duplicate is removed.
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # Add the current character to the window
            seen.add(s[right])

            # Update the maximum substring length
            longest = max(longest, right - left + 1)

        return longest
