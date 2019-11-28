# -*- coding: utf-8 -*-
"""
给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。
二叉搜索树(binary search tree, BST): 又称二叉查找树、二叉排序树，可以是一颗空树，若它的左子树不为空，则左子树所有结点的值均小于
它的根节点，若右子树不为空，则右子树结点的值均大于根节点，左右子树又分别为一棵二叉搜索树
案例 1:
输入:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9
输出: True
案例 2:
输入:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28
输出: False

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def findTarget(self, root, k):
        # 执行用时 96ms，内存消耗 16.2MB
        s = set()
        queue = [root]
        while queue:
            node = queue.pop(0)
            s.add(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        for num in s:
            if k - num in s and 2 * (k-num) != k:
                return True
        return False


