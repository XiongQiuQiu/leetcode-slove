# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        ans = []
        def findpossible(N):
            if N == 1: return TreeNode(0)
            for i in range(N-1):
                root = TreeNode(0)
                root.left = findpossible(i)
                root.right = findpossible(N-1-i)
                ans.append(root)
        return ans