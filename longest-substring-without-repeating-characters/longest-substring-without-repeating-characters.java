class Solution {
    public int lengthOfLongestSubstring(String s) {
     
        int left = 0;
        int right = 0;
        int longest = 0;
        int size = s.length();
        int currLongest = 0;
        HashMap<Character,Integer> map = new HashMap<>();
        
        if(size>0){
            map.put(s.charAt(left),1);
            longest = 1;
            right++;
        }
        
        while(right<size){
            
            if(map.containsKey(s.charAt(right))){
                while(left<right && map.containsKey(s.charAt(right))){
                    map.remove(s.charAt(left));
                    left++;
                }
            }
            else{
                currLongest = right - left + 1;
                if(currLongest>longest){
                    longest = currLongest;
                }
                map.put(s.charAt(right),1);
                right++;
            }
        }
        
        return longest;
        
    }
}