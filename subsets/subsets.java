class Solution {
    
    public static void backtrack(List<List<Integer>> res, int[] nums, int idx, ArrayList<Integer> currList){
        if(idx >= nums.length){
            res.add((ArrayList<Integer>)currList.clone());
            return;
        }
        
        backtrack(res,nums,idx+1,currList);
        currList.add(nums[idx]);
        backtrack(res,nums,idx+1,currList);
        currList.remove(currList.size() - 1);
        return;
    }
    
    public List<List<Integer>> subsets(int[] nums) {
        //List<List<Integer>> res = ArrayList<List<>>();
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        backtrack(res,nums,0,new ArrayList<Integer>());
        return res;
    }
}