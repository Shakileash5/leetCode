class Solution {
    public boolean checkIfExist(int[] arr) {
        Map<Integer,Integer> map = new HashMap<>();
        for(int n : arr) {
            if (map.getOrDefault(n*2,0) == 1) {
                return true;
            }
            else if(n%2 == 0 && map.getOrDefault(n/2,0) == 1) {
                return true;
            }
            if(map.getOrDefault(n, 0) == 0) {
                map.put(n,1);
            }
        }
        return false;
    }
}