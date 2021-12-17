class Solution {
    
    public static void getCombinations(ArrayList<Integer> currList, int sum, int[] candidates, int target, int idx, List<List<Integer>> combinations){
        if(sum == target){
            ArrayList<Integer> list = (ArrayList<Integer>)currList.clone();
            Collections.sort(list);
            if(combinations.contains(list) == false){
                combinations.add(list);
            }
            return;
        }
        if(idx>=candidates.length){
            return;
        }
        for(int i=idx;i<candidates.length;i++){
            if(sum+candidates[i]<=target){
                if(i>idx && candidates[i]==candidates[i-1]){
                    continue;
                }
                currList.add(candidates[i]);
                getCombinations(currList,sum+candidates[i],candidates,target,i+1,combinations);
                currList.remove(currList.size()-1);
            }
        }
        return;
    }
    
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> resCombinations = new ArrayList<List<Integer>>();
        getCombinations(new ArrayList<>(),0,candidates,target,0,resCombinations);
        return resCombinations;
    }
}