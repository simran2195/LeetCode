# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node, left, right):
            if node == None:
                return True # an empty tree is still a bst

            if not (node.val > left and node.val < right):
                return False # this node violates the condition

            
            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))


        return valid(root, float("-inf"), float("inf"))

        

        
        