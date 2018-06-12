# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        self.ans = []
        qa = [root]
        while qa:
            qb = []
            n = 0
            for i in qa:
                if i.left: qb.append(i.left)
                if i.right: qb.append(i.right)
                n += i.val
            self.ans.append(float(n)/len(qa))
            qa = qb
        return self.ans