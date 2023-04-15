class Solution {
    public int findNumbers(int[] nums) {
        int res = 0;
        for(int n : nums) {
            int noOfDigits = 0;
            while(n != 0) {
                noOfDigits++;
                n = n/10;
            }
            res += noOfDigits%2 == 0? 1 : 0;
        }

        return res;
    }
}