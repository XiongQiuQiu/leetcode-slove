'''

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        if not root.left and not root.right:
            return 1
        if not root.left: return self.minDepth(root.right) + 1
        if not root.right: return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left) + 1, self.minDepth(root.right) + 1)


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        res = 0
        queue = [root]

        while queue:
            size = len(queue)
            res += 1

            for i in xrange(size):
                tmp = queue.pop(0)

                if tmp.left is None and tmp.right is None:
                    return res

                if tmp.left is not None:
                    queue.append(tmp.left)

                if tmp.right is not None:
                    queue.append(tmp.right)

        return res