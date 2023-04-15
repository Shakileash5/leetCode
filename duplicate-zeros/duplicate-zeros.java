class Solution {
    public void duplicateZeros(int[] arr) {
        List<Integer> list = new ArrayList<>();
        int ptr = 0, temp = -1;
        while(ptr<arr.length) {
            if(temp!= -1) {
                if(arr[ptr] == 0) {
                    list.add(0);
                    list.add(0);
                }
                else {
                    list.add(arr[ptr]);
                }
                arr[ptr] = list.get(0);
                list.remove(0);

            }
            else {
                if(arr[ptr] == 0) {
                    temp = 0;
                    list.add(0);
                }
            }
            ptr += 1;
        }
    }
}