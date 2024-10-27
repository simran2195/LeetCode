# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs(left, right):
            # pass roots of left and right subtree
            # check left and right subtree of root
            if not left and not right:
                return True
            
            # if only 1 node is null and other isn't
            if not left or not right:
                return False

            # both nodes are not null
            # compare values of left and right node

            return ((left.val == right.val) and dfs(left.left, right.right) and dfs(right.left, left.right))
                
        return dfs(root.left, root.right)

        