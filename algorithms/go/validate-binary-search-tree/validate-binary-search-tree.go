/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isValidBST(root *TreeNode) bool {
	const MAXINT = int(^uint(0) >> 1)
	const MININT = ^MAXINT
	return recValidBST(root, MININT, MAXINT)
}

func recValidBST(root *TreeNode, min, max int) bool {
	if root == nil {
		return true
	}
	if root.Val <= min || root.Val >= max {
		return false
	}
	return recValidBST(root.Left, min, root.Val) && recValidBST(root.Right, root.Val, max)
}