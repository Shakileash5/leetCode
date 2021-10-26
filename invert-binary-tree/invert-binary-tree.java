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
    private TreeNode invertUtil(TreeNode root){
        if(root == null){
            return null;
        }
        TreeNode left = invertUtil(root.left);
        TreeNode right = invertUtil(root.right);
        root.left = right;
        root.right = left;
        return root;
    }
    
    public TreeNode invertTree(TreeNode root) {
        return this.invertUtil(root);    
    }
}