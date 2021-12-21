/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
 var isValidBST = function(root, flooring=Number.MIN_SAFE_INTEGER, ceiling=Number.MAX_SAFE_INTEGER) {
    if(!root) return true;
    if(root.val <= flooring || root.val >= ceiling) return false;
    return isValidBST(root.left, flooring, root.val) && isValidBST(root.right, root.val, ceiling);    
};