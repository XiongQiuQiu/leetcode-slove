
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.total = 0

        def traverse(root):
            if not root: return
            traverse(root.right)
            root.val += self.total
            self.total = root.val
            traverse(root.left)

        traverse(root)
        return root

l = TreeNode(2)
r = TreeNode(13)
ro = TreeNode(5)
ll = TreeNode(3)
rr = TreeNode(4)
ro.left = l
ro.right = r
l.left = ll
l.right = rr
l = [ro, l, rr, ll, rr]
ans = Solution()
print ans.convertBST(ro).val
ans_nu = [x.val for x in l]
