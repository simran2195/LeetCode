# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        q = collections.deque()
        q.append(root)
        
        while q:
            # iterate through 1 level at a time
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    # also add children of this node
                    q.append(node.left)
                    q.append(node.right)

            if level:
                res.append(level)
        
        return res

        