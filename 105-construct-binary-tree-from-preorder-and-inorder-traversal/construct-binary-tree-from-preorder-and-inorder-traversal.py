# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # base case
        if not preorder or not inorder:
            return None

        # Preorder -> Root, Left, Right
        # Inorder -> Left, Root, Right
        # Root = 1st element of preorder array

        # Create an object from the array value
        root = TreeNode(preorder[0])
        # now find root/mid in the inorder
        mid = inorder.index(preorder[0]) 

        # everything to the left of mid is the left subtree of the root
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid + 1:])

        return root


        