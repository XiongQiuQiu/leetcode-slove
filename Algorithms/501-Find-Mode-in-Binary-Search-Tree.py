'''

Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.


For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2


return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        stack = [root]
        tmp = []
        while stack:
            node = stack.pop()
            tmp.append(node.val)
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
        cnt = collections.Counter(tmp)
        maxfre = max(cnt.values())
        return [val for val in cnt if cnt[val] == maxfre]


class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # dfs inorder traverse to make sorted array
        if not root:
            return []
        stack = []
        maxx = count = 0
        pre = None
        res = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            if node.val == pre:
                count += 1
            else:
                count = 1
                pre = node.val
            if count >= maxx:
                if count > maxx:
                    res = []
                    maxx = count
                res.append(node.val)
            root = node.right
        return res
