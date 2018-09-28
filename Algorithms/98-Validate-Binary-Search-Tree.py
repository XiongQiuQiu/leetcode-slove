'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        ans = []

        def inorder(root):
            if not root: return
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)

        inorder(root)
        for i in range(1, len(ans)):
            if ans[i] <= ans[i - 1]: return False
        return True


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def push_all_left(self, node, stack):
        while node is not None:
            stack.append(node)
            node = node.left

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        # inorder traverse
        stack = []

        self.push_all_left(root, stack)
        last = float('-inf')

        while stack:
            cur = stack.pop()

            if cur.val <= last:
                return False

            last = cur.val

            if cur.right is not None:
                self.push_all_left(cur.right, stack)

        return True