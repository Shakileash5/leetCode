class Solution {
    public int maxArea(int[] height) {
     
        int maxArea = 0;
        int left = 0;
        int right = height.length - 1;
        int currArea = 0;
        
        while(left<right){
            currArea = Math.min(height[left],height[right])*(right-left);
            maxArea = Math.max(maxArea,currArea);
            
            if(height[left]<height[right]){
              left++;  
            }
            else{
                right--;
            }
        }
        
        return maxArea;
        
    }
}