# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        la = [root]
        while la:
            lb = []
            for x in la:
                if x.left: lb.append(x.left)
                if x.right: lb.append(x.right)
            if not lb: return la[0].val
            la = lb
        return None

