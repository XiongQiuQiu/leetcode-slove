'''
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example, given a 3-ary tree:





We should return its max depth, which is 3.

Note:

The depth of the tree is at most 1000.
The total number of nodes is at most 5000.

'''
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root: return 0
        queue = [(root, 1)]
        curdepth = 1
        while queue:
            for i in range(len(queue)):
                node, depth = queue.pop(0)
                if depth > curdepth:
                    curdepth = depth
                if node.children:
                    for chil in node.children:
                        queue.append((chil, depth + 1))
        return curdepth

