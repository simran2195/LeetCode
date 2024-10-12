# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = [] # to save the final array
        q = collections.deque() # initiate a deque
        q.append(root) # add the root to the q

        while q:
            qLen = len(q) # traverse for elements at each level 
            level = [] # create a sublist for that level's elements
            for i in range(qLen): # for all nodes in the queue
                node = q.popleft() # pop the left most element 
                if node:
                    level.append(node.val) # add value of node to the level result
                    q.append(node.left) # add left and right children to the queue
                    q.append(node.right)
            
            if level:
                res.append(level)
        return res
            

        