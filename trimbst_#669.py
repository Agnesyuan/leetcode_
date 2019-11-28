# -*- coding: utf-8 -*-
"""
给定一个二叉搜索树，同时给定最小边界L 和最大边界 R。通过修剪二叉搜索树，使得所有节点的值在[L, R]中 (R>=L) 。你可能需要改变树的根节点，所以结果应当返回修剪好的二叉搜索树的新的根节点。
示例 1:
输入:
    1
   / \
  0   2

  L = 1
  R = 2

输出:
    1
      \
       2

示例 2:
输入:
    3
   / \
  0   4
   \
    2
   /
  1

  L = 1
  R = 3

输出:
      3
     /
   2
  /
 1

1：当前节点为3，正好在范围内，修建左右子树
2：0为3的左节点，由于小于L，所以返回0->right，当0->right子树修改完成后，便拼接到0这个节点，这时3->left的节点便是0->right的修改树结构，从而实现拼接。

思路：递归遍历每一个节点检查是否在区间内
    如果节点为null直接返回null；如果节点小于L那么递归遍历右子节点返回；
    如果节点大于R那么递归遍历左子节点返回；如果节点在区间内，那么递归遍历左子节点作为新左子节点，递归遍历右子节点作为新右子节点，返回节点

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trimBST(self, root, L, R):
        # 执行用时 56ms，内存消耗 17.9MB
        if not  root:
            return root
        #import pdb;pdb.set_trace()
        if root.val < L:
            return self.trimBST(root.right, L, R)
        if root.val > R:
            return self.trimBST(root.left, L, R)
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left= TreeNode(0)
    root.right = TreeNode(2)
    print(s.trimBST(root, 1, 2))