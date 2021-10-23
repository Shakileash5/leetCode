class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        List<Integer> res = new ArrayList<>();
        
        int size = nums.length;
        int idx = 0;
        
        for(int i=0; i<size; i++){
            idx = Math.abs(nums[i])-1; // get idx of number          
            if(nums[idx]>0){ // check if index is already visited
                nums[idx] = -1 * nums[idx]; // mark the index as visited
            }
            else{
                
                res.add(Math.abs(nums[i]));
            }
            
        }
        
        return res;
    }
}