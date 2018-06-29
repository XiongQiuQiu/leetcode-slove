'''

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        def getpath(root, val):
            if root is None: return []
            if root.val == val and root.left is None and root.right is None:
                return [[root.val]]
            tmp = getpath(root.left, val - root.val) + getpath(root.right, val - root.val)
            return [[root.val] + i for i in tmp]

        return getpath(root, sum)



