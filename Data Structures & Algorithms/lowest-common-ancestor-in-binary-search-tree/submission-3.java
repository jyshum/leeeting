/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        // searching through this tree, the node we are tryin to find is where p and q are in its left and right tree (where it splits) -> that means the node is the closest to both, even if there are more parents down the line (BST)

        TreeNode cur = root;
        while (cur != null) {
            if (p.val < cur.val && q.val < cur.val) {
                // both p and q are in left side, search the left
                cur = cur.left; 
            } else if (p.val > cur.val && q.val > cur.val) {
                // both p and q are in the right side, search the right
                cur = cur.right;
            } else {
                // p and q are split up
                break;
            }
        }

        return cur;
    }
}
