# 116. Populating Next Right Pointers in Each Node
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        # Start with the leftmost node of the current level
        leftmost = root

        # Traverse levels until we reach the last level
        while leftmost.left:
            # Iterate through the current level
            head = leftmost
            while head:
                # Connect left child to right child
                head.left.next = head.right

                # Connect right child to the next node's left child (if exists)
                if head.next:
                    head.right.next = head.next.left

                # Move to the next node in the current level
                head = head.next

            # Move to the next level
            leftmost = leftmost.left

        return root

        