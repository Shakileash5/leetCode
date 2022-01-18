class Solution {
    
    public static boolean checkAdjacent(int[] flowerbed, int pos){
        
        int size = flowerbed.length;
        
        if(pos<0 && pos>=size){
            return false;
        }
        
        if(flowerbed[pos] == 1){
            return false;
        }
        
        if(pos-1 >= 0 ){
            if(pos+1<size){
                if(flowerbed[pos-1] == 0 && flowerbed[pos+1] == 0){
                    return true;
                }
            }
            else{
                if(flowerbed[pos-1] == 0){
                    return true;
                }
            }
        }
        else{
           if(pos+1<size){
               if(flowerbed[pos+1] == 0){
                   return true;
               }
           }
        }
        
        return false;
    }
    
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        
        int count = 0;
        boolean flag;
        
        if(flowerbed.length == 1 && n == 1 && flowerbed[0] == 0){
            return true;
        }
        if(n == 0){
            return true;
        }
        
        for(int i=0; i<flowerbed.length;){
            flag = false;
            if(flowerbed[i] == 0){
                if(checkAdjacent(flowerbed,i)){
                    count++;
                    flag = true;
                }
            }
            else{
                flag = true;
            }
            if(flag){
                i+=2;
            }
            else{
                i++;
            }
            if(count == n){
                break;
            }
        }
        
        if(count == n){
            return true;
        }
        return false;
        
    }
}