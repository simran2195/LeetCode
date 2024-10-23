# 1676. Lowest Common Ancestor of a Binary Tree IV
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        # Nodes -> an array of TreeNode objects nodes
        # and all values of the tree's nodes are unique.
        # return the lowest common ancestor (LCA) of all the nodes in nodes

        # definition of LCA on Wikipedia: "The lowest common ancestor of n nodes p1, p2, ..., pn 
        # in a binary tree T is the lowest node that has every pi as a descendant 
        # (where we allow a node to be a descendant of itself) for every valid i
        # ". A descendant of a node x is a node y that is on the path from node x to some leaf node.
        
        # use DFS to sole
        # transform nodes to a set to do a constant time lookup
        # lookup time in array in O(n)
        nodes = set(nodes)
        def dfs(node):
            if not node:
                return None

            if node in nodes:
                return node

            l = dfs(node.left)
            r = dfs(node.right)

            # if both l and r 
            if l and r:
                return node

            else:
                return l or r

        return dfs(root)
