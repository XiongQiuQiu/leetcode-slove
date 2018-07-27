'''
Given an n-ary tree, return the preorder traversal of its nodes' values.


For example, given a 3-ary tree:




Return its preorder traversal as: [1,3,5,6,2,4].


Note: Recursive solution is trivial, could you do it iteratively?
'''
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root: return []
        queue = [root]
        ans = []
        while queue:
            node = queue.pop(0)
            ans.append(node.val)
            if node.children: queue = node.children + queue
        return ans
