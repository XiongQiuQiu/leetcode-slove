import collections
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        cnt = collections.Counter()
        def subTreeSum(root):
            if not root: return 0
            return root.val + subTreeSum(root.left) + subTreeSum(root.right)
        def traverse(root):
            if not root: return
            cnt[subTreeSum(root)] += 1
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        maxfr = max(cnt.values())
        return [k for k,v in cnt.iteritems() if v == maxfr]