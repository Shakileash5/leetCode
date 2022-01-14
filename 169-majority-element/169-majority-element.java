class Solution {
    public int majorityElement(int[] nums) {
     
        // using boyer - moore majority voting
        int vote = 0;
        int size = nums.length;
        int candidate = -1;
        
        for(int i=0;i<size;i++){
            if(vote == 0){
                candidate = nums[i];
                vote = 1;
            }
            else{
                if(nums[i] == candidate){
                    vote++;
                }
                else{
                    vote--;
                }
            }
        }
        
        // now check if the majority is more than n/2
        int count = 0;
        for(int i=0;i<size;i++){
            if(nums[i] == candidate){
                count++;
            }
        }
        
        return candidate;
    }
}