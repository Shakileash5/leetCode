class Solution {
    public int minStartValue(int[] nums) {
        
        int sum = 0,i=0;
        int res = 0;
        
        while(i<nums.length){
            sum += nums[i];
            if(sum<res){
                res = sum;
            }
            i++;
            
        }
        
        
        return -1*res + 1;
        
    }
}