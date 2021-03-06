'''
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        def getpath(root):
            if root is None: return []
            if root.left is None and root.right is None:
                return [[root.val]]
            tmp = getpath(root.left) + getpath(root.right)
            return [[root.val] + i for i in tmp]

        return ['->'.join(str(i) for i in loop) for loop in getpath(root)]
