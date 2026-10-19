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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return true; // match of nodes (matched up)
        } else if (p == null || q == null) {
            return false; // (mismatch of node structure)
        } else if (p.val != q.val) {
            return false; // match of nodes (both not none, but mismatch of values)
        }

        boolean left = isSameTree(p.left, q.left); // check true on on left side of p and q
        boolean right = isSameTree(p.right, q.right); // check true on right side of p and q 

        return left && right; // both must be true
        
    }
}
