class Solution {
    public int removeDuplicates(int[] nums) {
        int firstDuplicate = 0, size = nums.length, totalDuplicates = 0;
        int ptr = 0, ptr2 = 0;
        while(ptr < size) {
            int temp = nums[ptr];
            while( ptr<size && (ptr-1) >= 0 && nums[ptr-1] == nums[ptr]) {
                ptr++;
            }
            if(ptr >= size) {
                break;
            }
            //System.out.println("s " + ptr2 + " " + ptr + " -- " + nums[ptr2] + " " + nums[ptr]);
            nums[ptr2] = nums[ptr];
            ptr++;
            ptr2++;
        }
        //System.out.println("res ::" + ptr2);
        return ptr2;
    }
}