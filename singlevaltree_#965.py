# -*- coding: utf-8 -*-
"""
如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。
只有给定的树是单值二叉树时，才返回 true；否则返回 false。
"""

class Solution:
    # one 实现方式和 numsum_#653相同，存入集合中，判断最后集合是否只剩一个元素（True）。
    # 执行用时 48ms，内存消耗 13.8MB
    # def isUnivalTree(self, root):
    #     s = set()
    #     queue = [root]
    #     while queue:
    #         node = queue.pop(0)
    #         s.add(node.val)
    #         if node.left:
    #             queue.append(node.left)
    #         if node.right:
    #             queue.append(node.right)
    #     if len(s) == 1:
    #             return True
    #     return False

    # two 执行用时52ms，内存消耗13.7MB
    def isUnivalTree(self, root):
        if (root.left and root.val != root.left.val) or (root.right and root.val != root.right.val):
            return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)