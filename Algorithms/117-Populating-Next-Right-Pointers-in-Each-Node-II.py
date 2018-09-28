'''

Given a binary tree

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
Example:

Given the following binary tree,

     1
   /  \
  2    3
 / \    \
4   5    7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \    \
4-> 5 -> 7 -> NULL

'''


# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root: return
        queue = [root]
        while queue:
            for i in range(len(queue)):
                if i == 0:
                    first = queue.pop(0)
                    if first.left: queue.append(first.left)
                    if first.right: queue.append(first.right)
                else:
                    node = queue.pop(0)
                    first.next = node
                    first = node
                    if i == len(queue) - 1: node.next = None
                    if node.left: queue.append(node.left)
                    if node.right: queue.append(node.right)


# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
"""
2rd
难点 在于不是满二叉树 就没办法直接连接了 用一个空间记录上一层的节点
会不会左节点 低于右边节点 (不能按照层次 每层不能用while start.left )

我的思路：BFS 层次 还是可以解（但是空间不符合） 每个节点存起来，然后把这个list拿出来去连

题解: 用一个指针 来模拟队列(因为有next指针 可以这么搞 保证可以往后层次遍历) 
最终head会是这一层的一条链



"""


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        dummy = TreeLinkNode(-999)
        cur = dummy  # cur是下一层的节点的链

        while root:  # root是上层节点
            # 1.left
            if root.left:
                cur.next = root.left
                cur = cur.next

            # 2.right
            if root.right:
                cur.next = root.right
                cur = cur.next

            # 这一层没有遍历完
            root = root.next  # 往后移动

            # 这一层遍历完了
            if not root:
                root = dummy.next  # root往下移一层

                dummy.next = None  # 还原下一层
                cur = dummy

