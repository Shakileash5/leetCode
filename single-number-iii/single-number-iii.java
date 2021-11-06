class Solution {
    public int[] singleNumber(int[] nums) {
        
        HashMap<Integer,Integer> map = new HashMap<>(); // HashMap to store occurances
        int[] arr = new int[2]; // result array
        int idx = 0;
        
        for(int i=0; i<nums.length; i++){
            if(map.containsKey(nums[i]) == true){ //if key is present increase occurance of item
                map.replace(nums[i],map.get(nums[i])+1);
            }
            else{ // if key not found then add to map
                map.put(nums[i],1);
            }
        }
        
        
        for(int key: map.keySet()){
            if(map.get(key) == 1){ // check for key witch occured only once
                arr[idx] = key;
                idx += 1;
            }
        }
        
        return arr;
    }
    
}