# LeetCode 5: Longest Palindromic Substring
# Difficulty: Medium
# Topic: String
#
# Approach:
# - Consider every character as the center of a palindrome.
# - Expand in both directions while the characters are equal.
# - Check both odd-length and even-length palindromes.
# - Keep track of the longest palindrome found.
#
# This is the solution using the Expand Around Center approach.
#
# Time Complexity: O(n²)
# Space Complexity: O(1)

class Solution(object):
    def longestPalindrome(self, s):

        # If the string is empty, return an empty string.
        if not s:
            return ""

        # Stores the starting and ending index
        # of the longest palindrome found.
        start = 0
        end = 0

        # Expands from the given center
        # and returns the palindrome boundaries.
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            # We move one extra step in the loop,
            # so return the previous valid indices.
            return left + 1, right - 1

        # Try every character as the center.
        for i in range(len(s)):

            # Check for odd length palindrome (aba)
            left1, right1 = expand(i, i)

            # Check for even length palindrome (abba)
            left2, right2 = expand(i, i + 1)

            # Update the answer if the odd palindrome is longer.
            if right1 - left1 > end - start:
                start = left1
                end = right1

            # Update the answer if the even palindrome is longer.
            if right2 - left2 > end - start:
                start = left2
                end = right2

        # Return the longest palindrome substring.
        return s[start:end + 1]
