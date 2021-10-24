class Solution {
    private boolean dfs(char[][] board, int i, int j, int idx, String word, Set<ArrayList<Integer>> visited){
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
        int x = 0 , y = 0;
        
        for(int idxRow=0; idxRow<dirs.length; idxRow++){
            x = i+dirs[idxRow][0];
            y = j+dirs[idxRow][1];
            if((0<=x && x<board.length) && (0<=y&& y<board[0].length)){
                if((word.charAt(idx) == board[x][y])){
                    if(visited.contains(new ArrayList<Integer>(Arrays.asList(x,y))) == false){
                         if(dfs(board,x,y,idx+1,word,visited)){
                            return true;
                        }
                    }
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
                    if(temp){ // if word is present return true
                        return true;
                    }
                    
                    
                    
                }
            }
        }
        
        return false;
    }
}