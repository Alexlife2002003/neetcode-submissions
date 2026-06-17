class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh=0
        q=deque()
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append((r,c))
        
        if fresh==0:
            return 0
        
        def addFruit(r, c):
            nonlocal fresh
            if r<0 or c<0 or r==rows or c==cols:
                return 
            
            if grid[r][c]!=1:
                return
            
            grid[r][c]=2
            fresh-=1
            q.append((r,c))
            
        res=-1
        while q :
            for i in range(len(q)):
                r, c = q.popleft()

                addFruit(r+1,c)
                addFruit(r,c+1)
                addFruit(r-1,c)
                addFruit(r,c-1)
            res+=1
        
        return res if fresh==0 else -1
        
        