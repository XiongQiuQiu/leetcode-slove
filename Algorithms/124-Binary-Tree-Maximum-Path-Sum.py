'''
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = None

        def search(root):
            if root is None: return 0
            leftmax = search(root.left)
            rightmax = search(root.right)
            self.ans = max(max(leftmax, 0) + max(rightmax, 0) + root.val, self.ans)
            return max(leftmax, rightmax, 0) + root.val

        search(root)
        return self.ans
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ms = [-4000000000]
        o = max_path(root, ms)
        return max(ms[0], o)

def max_path(root, ms):
	if root.left is None and root.right is None:
		return root.val
	if root.left is not None:
		l = max_path(root.left, ms)
	if root.right is not None:
		r = max_path(root.right, ms)
	if root.left is None:
		ms[0] = max(ms[0], r)
		return root.val + max(0, r)
	if root.right is None:
		ms[0] = max(ms[0], l)
		return root.val + max(0, l)
	ms[0] = max(ms[0], r, l, r + l + root.val)
	return root.val + max(0, r, l)