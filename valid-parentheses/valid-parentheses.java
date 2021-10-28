class Solution {
    
    private boolean checkBrackets(Character charOpen, Character charClose){
        
        if(charOpen == '(' && charClose == ')'){
            return true;
        }
        else if(charOpen == '{' && charClose == '}'){
            return true;
        }
        else if(charOpen == '[' && charClose == ']'){
            return true;
        }
        return false;
    }
    
    public boolean isValid(String s) {
        
        List<Character> stack = new ArrayList<>();
        int idx = 0;
        
        for(int i=0; i<s.length();i++){
            
            if(s.charAt(i) == '{' || s.charAt(i) == '(' || s.charAt(i) == '['){
                stack.add(s.charAt(i));
            }
            else{
                if(stack.size() == 0){
                    return false;
                }
                else if(this.checkBrackets(stack.remove(stack.size()-1),s.charAt(i)) == false){
                    return false;
                } 
            }
        }
        
        if(stack.size() != 0){
            return false;
        }
        
        return true;
    }
}