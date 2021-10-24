class Solution {
    private boolean dfs(char[][] board, int i, int j, int idx, String word, Set<ArrayList<Integer>> visited){
        //System.out.println(i+" "+j+" "+idx);
        //System.out.println(visited);
        //System.out.println(visited.contains(new ArrayList<Integer>(Arrays.asList(i,j))));
        if(idx >= word.length()){
            return true;
        }
        
        visited.add(new ArrayList<Integer>(Arrays.asList(i,j)));
        int[][] dirs = {
            {0, 1},
            {1, 0},
            {0, -1},
            {-1, 0}
        };
        
        for(int idxRow=0; idxRow<dirs.length; idxRow++){
    //System.out.println((i+dirs[idxRow][0])+"m "+j+dirs[idxRow][1]+"k "+board.length+" "+board[0].length);
            if((0<=(i+dirs[idxRow][0]) && (i+dirs[idxRow][0])<board.length) && (0<=(j+dirs[idxRow][1])&& (j+dirs[idxRow][1])<board[0].length)){
                //System.out.println(board[i+dirs[idxRow][0]][j+dirs[idxRow][1]]+" "+word.charAt(idx));
                if((word.charAt(idx) == board[i+dirs[idxRow][0]][j+dirs[idxRow][1]])){
                    if(visited.contains(new ArrayList<Integer>(Arrays.asList(i+dirs[idxRow][0],j+dirs[idxRow][1]))) == false){
                         if(dfs(board,i+dirs[idxRow][0],j+dirs[idxRow][1],idx+1,word,visited)){
                            return true;
                        }
                    }
                //idx += 1;
                    //System.out.println("i="+(i+dirs[idxRow][0])+"j="+(j+dirs[idxRow][1]));
                    
                   
                    //idx -= 1
                } 
            }
            
        
        }
        visited.remove(new ArrayList<Integer>(Arrays.asList(i,j)));
        return false;
    }
    
    public boolean exist(char[][] board, String word) {
        
        int sizeRow = board.length;
        int sizeCol = board[0].length;
        
        boolean temp;
        
        // run through every element 
        for(int i=0; i<sizeRow; i++){
            for(int j=0; j<sizeCol; j++){
                
                if(word.charAt(0) == board[i][j]){ // check if words starting letter and board elements matche's
                    Set<ArrayList<Integer>> visited = new HashSet<>();
                    temp = this.dfs(board,i,j,1,word,visited);
                    //System.out.printf("%d,%d",i,j);
                    //System.out.println(temp);
                    if(temp){
                        return true;
                    }
                    
                    
                    
                }
            }
        }
        
        return false;
    }
}