class Solution {
    
    private int dfs(int idxR, int idxC, int sizeR, int sizeC, int[][] memo){
        if(idxR == sizeR-1 && idxC == sizeC-1){
            return 1;
        }
        
        if(memo[idxR][idxC] == -1){
            int res = 0; // to store no of paths from current position
            if(idxC+1<sizeC){
                res += dfs(idxR,idxC+1,sizeR,sizeC,memo);    
            }
            if(idxR+1<sizeR){
                res += dfs(idxR+1,idxC,sizeR,sizeC,memo);
            }
            memo[idxR][idxC] = res;
        }
            
        return memo[idxR][idxC];
        
    }
    
    public int uniquePaths(int m, int n) {
        int[][] memo = new int[m][n];
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                memo[i][j] = -1;
            }
        }
        return this.dfs(0,0,m,n,memo);
        
    }
}