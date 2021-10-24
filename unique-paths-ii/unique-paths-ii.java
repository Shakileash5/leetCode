class Solution {
    
    private int dfs(int idxR, int idxC, int[][] grid, int[][] memo){
        if(idxR == grid.length-1 && idxC == grid[0].length-1){
            return 1;
        }
        
        if(memo[idxR][idxC] == -1){
            int res = 0;
            if(idxC+1 < grid[0].length && grid[idxR][idxC+1] == 0){
                res += dfs(idxR,idxC+1,grid,memo);
            }
            if(idxR+1 < grid.length && grid[idxR+1][idxC] == 0){
                res += dfs(idxR+1,idxC,grid,memo);
            }
            memo[idxR][idxC] = res;
        }
            
        return memo[idxR][idxC];
    }
    
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        if(obstacleGrid[0][0] == 1){
            return 0;
        }
        int[][] memo = new int[obstacleGrid.length][obstacleGrid[0].length];
        for(int i=0;i<obstacleGrid.length;i++){
            for(int j=0;j<obstacleGrid[0].length;j++){
                memo[i][j] = -1;
            }
        }
        return this.dfs(0,0,obstacleGrid,memo);
    }
}