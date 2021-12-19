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
    
    public static int recur(TreeNode root){
        if(root==null){
            return 0;
        }
        return Math.max(recur(root.left),recur(root.right)) + 1;
    }
    
    public int maxDepth(TreeNode root) {
        return recur(root);
    }
}