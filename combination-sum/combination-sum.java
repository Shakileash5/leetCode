class Solution {
    
    public static void recurSum(int[] candidates, ArrayList<Integer> currArr, List<List<Integer>> combinations, int idx, int target, int sum){
        
        if(sum == target){
            if(combinations.contains(currArr) == false){
                combinations.add((ArrayList<Integer>)currArr.clone());   
            }
            return;
        }
        else if(idx>=candidates.length){
            return;
        }
        
        if((sum + candidates[idx])<=target){
            currArr.add(candidates[idx]);
            recurSum(candidates,currArr,combinations,idx,target,sum+candidates[idx]);
            recurSum(candidates,currArr,combinations,idx+1,target,sum+candidates[idx]);
            currArr.remove(currArr.size()-1);
            
        }
        recurSum(candidates,currArr,combinations,idx+1,target,sum);
        
        return;
        
    }
    
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        
        List<List<Integer>> resCombinations = new ArrayList<List<Integer>>();
        recurSum(candidates,new ArrayList<Integer>(),resCombinations,0,target,0);
        return resCombinations;
    }
}