# -*- coding: utf-8 -*-
"""
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。一个节点也可以是它的祖先。
思路：root的值 在p、q中间，返回root； root值大于p、q，递归搜索右子树；反之 左子树
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 执行用时 84ms，内存消耗 17.8MB
class Solution:

    def lowestCommonAncestor(self, root, p, q):

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root