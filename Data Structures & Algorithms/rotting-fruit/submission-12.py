class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh=0
        minutes=0
        q=deque()
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append((r,c))
        
        def rotFruit(r,c):
            nonlocal fresh
            if r<0 or c<0 or r==rows or c==cols:
                return
            
            if grid[r][c]!=1:
                return
            
            grid[r][c]=2
            q.append((r,c))
            fresh-=1

        while q and fresh>0:
            for i in range(len(q)):
                r,c = q.popleft()
                
                rotFruit(r+1,c)
                rotFruit(r,c-1)
                rotFruit(r-1,c)
                rotFruit(r,c+1)
            minutes+=1
        
        return minutes if fresh==0 else -1
        

