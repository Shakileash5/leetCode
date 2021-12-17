class Solution {
    
    public static void recurCombination(String digits, String[] phoneNumber, int idx, String curr, List<String> resCombination){
        if(idx>=digits.length()){
            if(curr.equals("") == false){
                resCombination.add(curr);    
            }
            return;
        }
        int idxVal = digits.charAt(idx) - '0' - 2;
        for(int i=0; i<phoneNumber[idxVal].length();i++){
            recurCombination(digits,phoneNumber,idx+1,curr+phoneNumber[idxVal].charAt(i),resCombination);
        }
        return;
    }
    
    public List<String> letterCombinations(String digits) {
        
        String[] phoneNumber = {
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz"
        };
        ArrayList<String> resCombination = new ArrayList<>();
        //System.out.println(phoneNumber[0]);
        recurCombination(digits,phoneNumber,0,"",resCombination);
        
        return resCombination;
        
        
    }
}