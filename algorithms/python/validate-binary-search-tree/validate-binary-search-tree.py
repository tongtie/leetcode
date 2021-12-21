"""
// Source : https://leetcode.com/problems/validate-binary-search-tree/
// Author : Tong Tie
// Date   : 2021-12-20

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 10的4方].
-2的31方 <= Node.val <= 2的31方 - 1
"""

"""
思路：
根据二叉搜索树定义， 我们知道， 左子树的所有节点的值都小于根节点的值， 右子树的所有节点的值都大于根节点的值。
那么计算左子树的时候，我们传递根节点的数给他，因为根节点是左子树的最大值，只要左子树所有的节点的值都小于根节点的值，那么左子树就是二叉搜索树。（不需要考虑最小值）
同理计算右子树。

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], flooring=float('-inf'), ceiling=float('inf')) -> bool:
        if root is None:
            return True
        if root.val <= flooring or root.val >= ceiling:
            return False
        return self.isValidBST(root.left, flooring, root.val) and self.isValidBST(root.right, root.val, ceiling)
