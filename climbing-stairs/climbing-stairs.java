class Solution {
    public int climbStairs(int n) {
     
        int step1 = 1;
        int step2 = 1;
        
        if(n <= 1){ // base case 
            return step1;
        }
        
        int res = 0;
        
        for(int i=1;i<n;i++){ // run until n create fibnacci
            res = step1 + step2;
            step2 = step1;
            step1 = res;
        }
        
        return res;
        
    }
}