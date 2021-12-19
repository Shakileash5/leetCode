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
    
    public static TreeNode buildTreeHelper(int[] preorder, int[] inorder, int[] idx,int left, int right){
        if(left>right){
            return null;
        }
        
        TreeNode node = new TreeNode(preorder[idx[0]]);
        int inorderIdx = searchIdx(inorder,left,right,preorder[idx[0]]);
        idx[0]++;
        if(left == right){
            return node;
        }
        
        node.left = buildTreeHelper(preorder,inorder,idx,left,inorderIdx-1);
        node.right = buildTreeHelper(preorder,inorder,idx,inorderIdx+1,right);
        return node;
        
    }
    
    public static int searchIdx(int[] inorder, int left, int right, int target){
        
        for(int i=left;i<=right;i++){
            if(inorder[i] == target){
                return i;
            }
        }
        return -1;
    }
    
    
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        int[] idx = new int[1];
        idx[0] = 0;
        return buildTreeHelper(preorder,inorder,idx,0,preorder.length-1);
    }
}