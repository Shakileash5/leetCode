class Solution {
    public String longestCommonPrefix(String[] strs) {
        
        int idx = 0;
        int size = strs.length;
        int charIdx = 0;
        String longestPrefix = "";
        boolean flag = false;
        char currChar;
        
        while(true){
            flag = false;
            if(charIdx < strs[0].length()){
                currChar = strs[0].charAt(charIdx);    
            }
            else{
                break;
            }
                 
            while(idx<size){
                if(charIdx < strs[idx].length()){
                    if(strs[idx].charAt(charIdx) != currChar){
                        flag = true;
                        break;
                    }
                }
                else{
                    flag = true;
                    break;
                }
                idx++;
            }
            
            if(flag == false){
                longestPrefix = longestPrefix + currChar;
            }
            else{
                break;
            }
            
            idx = 0;
            charIdx++;
            
        }
        
        return longestPrefix;
        
    }
}