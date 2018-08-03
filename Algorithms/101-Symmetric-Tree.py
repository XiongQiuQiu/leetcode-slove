'''

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.


'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        if root.left and root.right and root.left.val == root.right.val:
            left = [root.left]
            right = [root.right]
        elif root.left or root.right:
            return False
        else:
            return True
        while left and right:
            for i in range(len(left)):
                l = left.pop()
                r = right.pop()
                if l.left and r.right:
                    if l.left.val != r.right.val:
                        return False
                    left.append(l.left)
                    right.append(r.right)
                elif l.left or r.right:
                    return False
                if l.right and r.left:
                    if l.right.val != r.left.val:
                        return False
                    left.append(l.right)
                    right.append(r.left)
                elif l.right or r.left:
                    return False
        return True

    def isSymmetric(self, root):
        def isSym(L, R):
            if not L and not R: return True
            if L and R and L.val == R.val:
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return False

        return isSym(root, root)