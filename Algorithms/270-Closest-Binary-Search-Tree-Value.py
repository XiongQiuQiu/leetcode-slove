'''
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.

'''
class Solution():
    def cosestValue(self,root,target):
        if not root : return None
        ans = abs(root.val-target)
        while True:
            if abs(root.val-target) < ans:
                ans = abs(root.val-target)
                ans_val = root.val
            if target < root.val and root.left:
                root = root.left
            elif target > root.val and root.right:
                root = root.right
            else: break
        return ans_val
