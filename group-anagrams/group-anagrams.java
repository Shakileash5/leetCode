class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
        HashMap<String,ArrayList<String>> map = new HashMap<>();
        List<List<String>> res = new ArrayList<List<String>>();
        int size = strs.length;
        String temp = "";
        
        for(String str : strs){
            temp = str;
            char[] tempCh = temp.toCharArray();
            Arrays.sort(tempCh);
            temp = new String(tempCh);
            
            if(map.containsKey(temp)){
                map.get(temp).add(str);
            }
            else{
                map.put(temp,new ArrayList<String>());
                map.get(temp).add(str);
            }
        }
        
        for(ArrayList<String> arr: map.values()){
            res.add(arr);
        }
        return res;
    }
}