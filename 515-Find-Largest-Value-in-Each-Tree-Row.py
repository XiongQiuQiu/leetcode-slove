# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        qa, ans = [root], []
        while qa:
            maxn = None
            qb = []
            for i in qa:
                maxn = max(i.val, maxn)
                if i.left: qb.append(i.left)
                if i.right: qb.append(i.right)
            ans.append(maxn)
            qa = qb
        return ans
        