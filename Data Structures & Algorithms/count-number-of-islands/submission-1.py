class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c]!="1":
                return
            
            grid[r][c]="X"

            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=="1":
                    dfs(row,col)
                    total+=1
        
        return total

        