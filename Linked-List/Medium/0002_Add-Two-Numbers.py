# LeetCode 2: Add Two Numbers
# Difficulty: Medium
# Topic: Linked List, Math

# Approach:
# - Traverse both linked lists simultaneously.
# - Add the corresponding digits along with any carry
#   from the previous addition.
# - Store the last digit of the sum in a new node.
# - Carry the remaining value to the next iteration.
# - If one list is shorter, treat its missing digits as 0.
# - After the traversal, add a final node if a carry remains.

# This is the optimal solution.

# Time Complexity: O(max(m, n))
# where:
# m = length of the first linked list
# n = length of the second linked list

# Space Complexity: O(max(m, n))
# (The output linked list stores the result.)

'''Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''

class Solution(object):
    def addTwoNumbers(self, l1, l2):

        # Pointers to traverse both linked lists.
        current_l1, current_l2 = l1, l2

        # Dummy node simplifies building the result list.
        ans = ListNode(0)
        current = ans

        # Stores the carry from the previous addition.
        carry = 0

        # Continue until both linked lists are fully traversed.
        while current_l1 is not None or current_l2 is not None:

            # Use 0 if a linked list has no more nodes.
            val1 = current_l1.val if current_l1 else 0
            val2 = current_l2.val if current_l2 else 0

            # Calculate the sum of the current digits and carry.
            num = val1 + val2 + carry

            # Update the carry and keep only the current digit.
            if num >= 10:
                carry = num // 10
                num = num % 10
            else:
                carry = 0

            # Add the current digit to the result list.
            current.next = ListNode(num)
            current = current.next

            # Move to the next node in the first list.
            if current_l1:
                current_l1 = current_l1.next

            # Move to the next node in the second list.
            if current_l2:
                current_l2 = current_l2.next

        # If a carry remains, add it as the last node.
        if carry:
            current.next = ListNode(carry)

        # Return the result linked list,
        # skipping the dummy node.
        return ans.next
