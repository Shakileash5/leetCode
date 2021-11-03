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
    private int rootToLeaf(TreeNode root, int[] totalSum, String value){
        
        if(root == null){
            return 0;
        }
        
        if(root.left == null && root.right == null){
            //System.out.println(value+"leaf");
            totalSum[0] += Integer.parseInt(value+ root.val) ;
        }
        rootToLeaf(root.left,totalSum,value + Integer.toString(root.val));
        rootToLeaf(root.right,totalSum,value + Integer.toString(root.val));
        return totalSum[0];
    }
    public int sumNumbers(TreeNode root) {
        
        int[] totalSum = {0};
        int sum = rootToLeaf(root,totalSum,"");
        return sum;
    }
}