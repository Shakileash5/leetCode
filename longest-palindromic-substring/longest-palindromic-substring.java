class Solution {
    public String longestPalindrome(String s) {
        
        int maxLength = 0;
        int resStartIdx = 0;
        int resEndIdx = 0;
        int startIdx = 0;
        int endIdx = 0;
        
        for(int i=1; i<s.length();i++){
            
            // check if there forms an even palindrome
            startIdx = i-1;
            endIdx = i+1;
            
            while((startIdx>=0 && endIdx<s.length()) && (s.charAt(startIdx) == s.charAt(endIdx))){
                if((endIdx - startIdx + 1) > maxLength){
                    maxLength = endIdx - startIdx + 1;
                    resStartIdx = startIdx;
                    resEndIdx = endIdx;
                }
                startIdx--;
                endIdx++;
            }
            
            // check if there forms an odd palindrome
            startIdx = i-1;
            endIdx = i;
            
            while((startIdx>=0 && endIdx<s.length()) && (s.charAt(startIdx) == s.charAt(endIdx))){
                if((endIdx - startIdx + 1) > maxLength){
                    maxLength = endIdx - startIdx + 1;
                    resStartIdx = startIdx;
                    resEndIdx = endIdx;
                }
                startIdx--;
                endIdx++;
            }
            
        }
        
        //System.out.println(maxLength+" "+resStartIdx+" "+resEndIdx);
        return s.substring(resStartIdx,resEndIdx+1);
        
    }
}