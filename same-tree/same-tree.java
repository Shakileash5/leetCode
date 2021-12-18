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
    
    public static boolean isSame(TreeNode p, TreeNode q){
        if(p == null && q == null){
            return true;
        }
        else if(p == null || q == null){
            return false;
        }
        
        
        boolean flag1 = true, flag2 = true;
        flag1 = isSame(p.left,q.left);
        if( p.val != q.val){
            return false;  
        }
        flag2 = isSame(p.right,q.right);
        if(flag1 == false || flag2 == false){
            return false;
        }
        return true;
    }
    
    public boolean isSameTree(TreeNode p, TreeNode q) {
        return isSame(p,q);
    }
}