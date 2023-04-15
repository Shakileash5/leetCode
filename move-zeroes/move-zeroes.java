class Solution {
    public void moveZeroes(int[] nums) {
        int readPtr = 0;
        int writePtr = 0;

        for(readPtr = 0; readPtr<nums.length; readPtr++) {
            if(nums[readPtr] == 0) {
                continue;
            }
            nums[writePtr] = nums[readPtr];
            writePtr++;
        }
        while(writePtr < nums.length) {
            nums[writePtr] = 0;
            writePtr++;
        }
    }
}